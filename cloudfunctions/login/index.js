// 云函数入口文件
const cloud = require('wx-server-sdk')

// 初始化 cloud
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV // 使用当前环境
})

// 初始化数据库
const db = cloud.database()
const usersCollection = db.collection('users')

// 云函数入口函数
exports.main = async (event, context) => {
  const wxContext = cloud.getWXContext()
  const openid = wxContext.OPENID

  try {
    // 查询 'users' 集合中是否存在该用户
    const userResult = await usersCollection.where({
      openid: openid
    }).get()

    if (userResult.data.length === 0) {
      // 如果用户不存在，创建新用户
      const newUser = await usersCollection.add({
        data: {
          openid: openid,
          nickname: event.nickname || '新用户',
          avatarUrl: event.avatarUrl || '',
          createdAt: db.serverDate(), // 使用服务器时间
          updatedAt: db.serverDate()
        }
      })

      // 查询新创建的用户信息
      const createdUser = await usersCollection.doc(newUser._id).get()

      return {
        openid: openid,
        userInfo: createdUser.data
      }
    } else {
      // 用户已存在，返回用户信息
      return {
        openid: openid,
        userInfo: userResult.data[0]
      }
    }
  } catch (err) {
    // 错误处理
    console.error('云函数执行失败：', err)
    return {
      success: false,
      error: err.message
    }
  }
}
