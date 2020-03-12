function Banner() {

}

Banner.prototype.listenAddBannerEvent = function(){
    var self = this;
    var addBtn = $("#add-banner-btn");
    addBtn.click(function () {
        var tpl = template("banner-item");
        var bannerListGroup = $(".banner-list-group");
        bannerListGroup.prepend(tpl);

        var bannerItem = bannerListGroup.find(".banner-item:first");

        self.addImageSelectEvent(bannerItem);

    })
};

Banner.prototype.addImageSelectEvent = function(bannerItem){
    var image = bannerItem.find(".thumbnail");
    var imageInput = bannerItem.find(".image-input");

    image.click(function () {
        imageInput.click();
    });

    imageInput.change(function () {
        var file = this.files[0];
        var formData = new FormData();
        formData.append("file", file);
        xfzajax.post({
            "url": "/cms/upload_file/",
            "data": formData,
            "processData": false,
            "contentType": false,
            "success": function (result) {
                if(result["code"] === 200){
                    var url = result["data"]["url"];
                }
            }
        })

    })
};

Banner.prototype.run = function () {
    var self = this;
    self.listenAddBannerEvent();
};

$(function () {
    var banner = new Banner();
    banner.run();
});