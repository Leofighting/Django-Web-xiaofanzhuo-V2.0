function News() {

}

// 将文件上传至本地服务器
News.prototype.listenUploadFileEvent = function () {
    var uploadBtn = $("#thumbnail-btn");
    uploadBtn.change(function () {
        var file = uploadBtn[0].files[0];
        var formData = new FormData();
        formData.append("file", file);
        xfzajax.post({
            "url": "/cms/upload_file/",
            "data": formData,
            "processData": false,
            "contentType": false,
            "success": function (result) {
                if (result["code"] === 200) {
                    var url = result["data"]["url"];
                    var thumbnailInput = $("#thumbnail-form");
                    thumbnailInput.val(url);
                }
            }
        })
    })
};

// 将文件上传至七牛云
News.prototype.listenQiniuFileEvent = function () {
    var self = this;
    var uploadBtn = $("#thumbnail-btn");
    uploadBtn.change(function () {
        var file = this.files[0];
        xfzajax.get({
            "url": "/cms/qntoken/",
            "success": function (result) {
                if (result["code"] === 200) {
                    var token = result["data"]["token"];
                    var key = (new Date()).getTime() + "." + file.name.split(".")[-1];
                    var putExtra = {
                        fname: key,
                        params: {},
                        mimeType: ["image/png", "image/jpeg", "image/gif"]

                    };
                    var config = {
                        useCdnDomain: true,
                        retryCount: 6,
                        region: qiniu.region.z0
                    };
                    var observable = qiniu.upload(file, key, token, putExtra, config);
                    observable.subscribe({
                        "next": self.handleFileUploadProgress,
                        "error": self.handleFileUploadError,
                        "complete": self.handleFileUploadComplete
                    })
                }
            }
        })
    })
};

News.prototype.handleFileUploadProgress = function (response) {
    var total = response.total;
    var percent = total.percent;
    var progressGroup = News.progressGroup;
    progressGroup.show();
    var progressBar = $(".progress-bar");
    progressBar.css({"width": percent.toFixed(0) + "%"});
    progressBar.text(percent.toFixed(0) + "%");
};

News.prototype.handleFileUploadError = function (error) {
    window.messageBox.showError(error.message);
    var progressGroup = $("#progress-group");
    progressGroup.hide();
    console.log(error.message);
};

News.prototype.handleFileUploadComplete = function (response) {
    console.log(response);
    var progressGroup = $("#progress-group");
    progressGroup.hide();

    var domain = 'http://7xqenu.com1.z0.glb.clouddn.com/';
    var filename = response.key;
    var url = domain + filename;
    var thumbnailInput = $("input[name='thumbnail']");
    thumbnailInput.val(url);

};

News.prototype.initUEditor = function () {
    window.ue = UE.getEditor("editor", {
        "initialFrameHeight": 500,
        "serverUrl": "/ueditor/upload/"
    });

};

News.prototype.listenSubmitEvent = function () {
    var submitBtn = $("#submit-btn");
    submitBtn.click(function (event) {
        event.preventDefault();
        var title = $("input[name='title']").val();
        var category = $("select[name='category']").val();
        var desc = $("input[name='desc']").val();
        var thumbnail = $("input[name='thumbnail']").val();
        var content = window.ue.getContent();

        xfzajax.post({
            "url": "/cms/write_news/",
            "data": {
                "title": title,
                "category": category,
                "desc": desc,
                "thumbnail": thumbnail,
                "content": content
            },
            "success": function (result) {
                if (result["code"] === 200) {
                    xfzalert.alertSuccess("新闻发表成功~", function () {
                        window.location.reload();
                    })
                }

            }
        })

    })
}

News.prototype.run = function () {
    var self = this;
    self.listenUploadFileEvent();
    self.initUEditor();
    self.listenSubmitEvent();
};

$(function () {
    var news = new News();
    news.run();
    News.progressGroup = $("#progress-group");
});