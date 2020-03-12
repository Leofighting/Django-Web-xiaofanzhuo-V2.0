function Banner() {
    this.index = 1;
    this.bannerWidth = 798;
    this.leftArrow = $(".left-arrow");
    this.rightArrow = $(".right-arrow");
    this.bannerUl = $("#banner-ul");
    this.liList = this.bannerUl.children("li");
    this.bannerCount = this.liList.length;
    this.bannerGroup = $("#banner-group");
    this.pageControl = $(".page-control");
};

Banner.prototype.initBanner = function () {
    var self = this;
    var firstBanner = self.liList.eq(0).clone();
    var lastBanner = self.liList.eq(self.bannerCount - 1).clone();
    self.bannerUl.append(firstBanner);
    self.bannerUl.prepend(lastBanner);
    self.bannerUl.css({"width": self.bannerWidth * (self.bannerCount + 2), "left": -self.bannerWidth});
};

Banner.prototype.initPageControl = function () {
    var self = this;
    for (var i = 0; i < self.bannerCount; i++) {
        var circle = $("<li></li>");
        self.pageControl.append(circle);
        if (i === 0) {
            circle.addClass("active");
        }
    }
    self.pageControl.css({"width": self.bannerCount * 28});
};

Banner.prototype.animate = function () {
    var self = this;
    self.bannerUl.animate({"left": -798 * self.index}, 750);
    var index = self.index;
    if (index === 0) {
        index = self.bannerCount - 1;
    } else if (index === self.bannerCount + 1) {
        index = 0;
    } else {
        index = self.index - 1;
    }
    self.pageControl.children("li").eq(index).addClass("active").siblings().removeClass("active");
};

Banner.prototype.toggleArrow = function (isShow) {
    if (isShow) {
        this.leftArrow.show();
        this.rightArrow.show();
    } else {
        this.leftArrow.hide();
        this.rightArrow.hide();
    }
    ;
};


Banner.prototype.loop = function () {
    var self = this;
    var bannerUl = $("#banner-ul");
    this.timer = setInterval(function () {
        if (self.index >= self.bannerCount + 1) {
            self.bannerUl.css({"left": -self.bannerWidth});
            self.index = 2;
        } else {
            self.index++
        }
        ;
        self.animate();
    }, 2000);
};

Banner.prototype.listenArrowClick = function () {
    var self = this;
    self.leftArrow.click(function () {
        if (self.index === 0) {
            self.bannerUl.css({"left": -self.bannerCount * self.bannerWidth})
            self.index = self.bannerCount - 1;
        } else {
            self.index--;
        }
        self.animate();
    });
    self.rightArrow.click(function () {
        if (self.index === self.bannerCount + 1) {
            self.bannerUl.css({"left": -self.bannerWidth});
            self.index = 2;
        } else {
            self.index++;
        }
        self.animate();
    })
};

Banner.prototype.listenBannerHover = function () {
    var self = this;
    this.bannerGroup.hover(function () {
        // 鼠标进入事件
        clearInterval(self.timer);
        self.toggleArrow(true);
    }, function () {
        // 鼠标离开事件
        self.loop();
        self.toggleArrow(false);
    });
};

Banner.prototype.listenPageControl = function () {
    var self = this;
    self.pageControl.children("li").each(function (index, obj) {
        $(obj).click(function () {
            self.index = index;
            self.animate();

        });
    });
};

Banner.prototype.run = function () {
    this.initBanner();
    this.initPageControl();
    this.loop();
    this.listenArrowClick();
    this.listenBannerHover();
    this.listenPageControl();

};

function Index() {
    var self = this;
    self.page = 2;
    self.category_id = 0;
    self.loadBtn = $("#load-more-btn");

    template.defaults.imports.timeSince = function (dateValue) {
        var date = new Date(dateValue);
        var datets = date.getTime();
        var nowts = (new Date()).getTime();
        var timestamp = (nowts - datets) / 1000;
        if (timestamp < 60) {
            return "刚刚";
        } else if (timestamp >= 60 && timestamp < 60 * 60) {
            minutes = parseInt(timestamp / 60);
            return minutes + "分钟前";
        } else if (timestamp >= 60 * 60 && timestamp < 60 * 60 * 24) {
            hours = parseInt(timestamp / 60 / 60);
            return hours + "小时前";
        } else if (timestamp >= 60 * 60 * 24 && timestamp < 60 * 60 * 24 * 30) {
            days = parseInt(timestamp / 60 / 60 / 24);
            return days + "天前";
        } else {
            var year = date.getFullYear();
            var month = date.getMonth() + 1;
            var day = date.getDay();
            var hour = date.getHours();
            var minute = date.getMinutes();
            return year + "/" + month + "/" + day + " " + hour + ":" + minute;
        }

    }
}

Index.prototype.listenLoadMoreEvent = function () {
    var self = this;
    self.loadBtn.click(function () {
        xfzajax.get({
            "url": "/news/news_list/",
            "data": {
                "p": self.page,
                "category_id": self.category_id
            },
            "success": function (result) {
                if (result["code"] === 200) {
                    var newses = result["data"];
                    if (newses.length > 0) {
                        var tpl = template("news-item", {"newses": newses});
                        var ul = $(".list-inner-group");
                        ul.append(tpl);
                        self.page += 1;
                    } else {
                        self.loadBtn.hide();
                    }
                }
            }
        })
    })
};

Index.prototype.listenCategorySwitchEvent = function () {
    var self = this;
    var tabGroup = $(".list-tab");
    tabGroup.children().click(function () {
        var li = $(this);
        var category_id = li.attr("data-category");
        var page = 1;
        xfzajax.get({
            "url": "/news/news_list/",
            "data": {
                "category_id": category_id,
                "p": page
            },
            "success": function (result) {
                if (result["code"] === 200) {
                    var newses = result["data"];
                    var tpl = template("news-item", {"newses": newses});
                    var newsListGroup = $(".list-inner-group");
                    newsListGroup.empty();
                    newsListGroup.append(tpl);
                    self.page = 2;
                    self.category_id = category_id;
                    li.addClass("active").siblings().removeClass("active");
                    self.loadBtn.show();
                }

            }
        })

    })
};

Index.prototype.run = function () {
    var self = this;
    self.listenLoadMoreEvent();
    self.listenCategorySwitchEvent()
};

$(function () {
    var banner = new Banner();
    banner.run();

    var index = new Index();
    index.run();
});