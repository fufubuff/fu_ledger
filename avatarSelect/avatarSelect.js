Page({
  data: {
    currentAvatar: '', // 当前头像
    defaultAvatars: [
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar1.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar2.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar3.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar4.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar5.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar6.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar7.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar8.jpg',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar9.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar10.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar11.png',
      'cloud://fufubuff-3gt0b01y042179cc.6675-fufubuff-3gt0b01y042179cc-1330048678/images/avatars/avatar12.png'
    ],
    selectedAvatar: '' // 用户选择的新头像
  },
  onLoad: function (options) {  
    this.setData({  
      currentAvatar: options.currentAvatar || 'cloud://fufubuff-3gt0b01y042179cc-6675-fufubuff-3gt0b01y042179cc-1330048678/images/default-avatar.jpg',  
      selectedAvatar: options.currentAvatar || 'cloud://fufubuff-3gt0b01y042179cc-6675-fufubuff-3gt0b01y042179cc-1330048678/images/default-avatar.jpg'  
    });  
  },  
  
  selectAvatar: function (e) {  
    const selectedUrl = e.currentTarget.dataset.url;  
    this.setData({  
      selectedAvatar: selectedUrl  
    });  
  },  
  
  confirmSelection: function () {  
    const { selectedAvatar } = this.data;  
    const pages = getCurrentPages();  
    const prevPage = pages[pages.length - 2];  

    // 检查 prevPage 是否存在，并确保是 my 页面
    if (prevPage && prevPage.route === 'pages/my/my') {
      prevPage.setData({  
          currentAvatar: selectedAvatar // 传递选中的头像  
      });  
      wx.navigateBack();  
  } else {
      wx.showToast({
          title: '未找到前一个页面',
          icon: 'none'
      });
  }
}

});
