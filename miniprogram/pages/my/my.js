let app = getApp();
Page({
  data: {
    footerIndex: 3,
    menus: [],
    backgroundImage: '/utils/icons/background.jpg', // 默认背景图片
    avatarUrl: '/utils/icons/default_avatar.png' // 默认头像图片
  },
  onLoad: function (options) {
    this.setMenus();
    this.loadBackgroundImage();
    this.loadAvatar();
  },
  onShow: function () {

  },
  setMenus(){ // 初始化菜单 
    this.setData({
      menus: [
        {
          name: '计划',
          icon: 'icon_178',
          path: 'planList'
        }
      ]
    });
  },
  menuClick(e){ // 点击菜单选项
    let idx = e.currentTarget.dataset.idx;
    let path = this.data.menus[idx].path;
    app.navigate(`/pages/${path}/${path}`);
  },
  changeFooter(e) {
    app.changeFooter(e);
  },
  changeBackgroundClick(e) { // 点击更换背景
    let that = this;
    wx.chooseImage({
      count: 1,
      sizeType: ['original', 'compressed'],
      sourceType: ['album', 'camera'],
      success(res) {
        // 设置背景图片
        that.setData({
          backgroundImage: res.tempFilePaths[0]
        });
        // 持久化存储背景图片路径
        wx.setStorageSync('backgroundImage', res.tempFilePaths[0]);
      }
    });
  },
  changeAvatarClick(e) { // 点击更换头像
    let that = this;
    wx.chooseImage({
      count: 1,
      sizeType: ['original', 'compressed'],
      sourceType: ['album', 'camera'],
      success(res) {
        // 设置头像图片
        that.setData({
          avatarUrl: res.tempFilePaths[0]
        });
        // 持久化存储头像图片路径
        wx.setStorageSync('avatarUrl', res.tempFilePaths[0]);
      }
    });
  },
  loadBackgroundImage() {
    // 从本地存储中加载背景图片
    const backgroundImage = wx.getStorageSync('backgroundImage');
    if (backgroundImage) {
      this.setData({
        backgroundImage: backgroundImage
      });
    }
  },
  loadAvatar() {
    // 从本地存储中加载头像图片
    const avatarUrl = wx.getStorageSync('avatarUrl');
    if (avatarUrl) {
      this.setData({
        avatarUrl: avatarUrl
      });
    }
  }
});