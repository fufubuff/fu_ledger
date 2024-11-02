Page({
  data: {
    backgroundColor: '#ffffff' // 默认背景颜色
  },
  changeBackgroundColor(e) {
    this.setData({
      backgroundColor: e.detail.value
    });
  },
  applyBackgroundColor() {
    getApp().globalData.backgroundColor = this.data.backgroundColor;
    wx.showToast({
      title: '背景颜色已应用',
      icon: 'icon_178',
      duration: 2000
    });
  }
})