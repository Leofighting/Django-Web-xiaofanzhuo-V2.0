function CMSNewsList() {

}

CMSNewsList.prototype.initDatePicker = function () {
    var startPicker = $("#start-picker");
    var endPicker = $("#end-picker");

    var todayDate = new Date();
    var todayStr = todayDate.getFullYear() + "/" + (todayDate.getMonth() + 1) + "/" + todayDate.getDate();
    var options = {
        "showButtonPanel": true,
        "format": "yyyy/mm/dd",
        "startDate": "2020/1/1",
        "endDate": todayStr,
        "language": "zh-CN",
        "todayBtn": "linked",
        "todayHighlight": true,
        "clearBtn": true,
        "autoclose": true
    };
    startPicker.datepicker(options);
    endPicker.datepicker(options);
};

CMSNewsList.prototype.listenDeleteEvent = function () {
    var deleteBtn = $(".delete-btn");
    deleteBtn.click(function () {
        var btn = $(this);
        var news_id = btn.attr("data-news-id");
        xfzalert.alertConfirm({
            "text": "您确定要删除此新闻？",
            "confirmCallback": function () {
                xfzajax.post({
                    "url": "/cms/delete_news/",
                    "data": {
                        "news_id": news_id
                    },
                    "success": function (result) {
                        if (result["code"] === 200) {
                            window.location.reload();
                        }
                    }
                })
            }
        })
    })
};

CMSNewsList.prototype.run = function () {
    var self = this;
    self.initDatePicker();
    self.listenDeleteEvent();

};

$(function () {
    var newsList = new CMSNewsList();
    newsList.run();
});