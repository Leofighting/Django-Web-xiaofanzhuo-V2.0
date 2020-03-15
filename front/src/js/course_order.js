function CourseOrder() {

}

CourseOrder.prototype.listenPayEvent = function () {
    var submitBtn = $("#submit-btn");
    submitBtn.click(function (event) {
        event.preventDefault();
        var goodsname = $("input[name='goodsname']").val();
        var istype = $("input[name='istype']:checked").val();
        var notify_url = $("input[name='notify_url']").val();
        var orderid = $("input[name='orderid']").val();
        var price = $("input[name='price']").val();
        var return_url = $("input[name='return_url']").val();
        xfzajax.post({
            'url': '/course/course_order_key/',
            'data': {
                'goodsname': goodsname,
                'istype': istype,
                'notify_url': notify_url,
                'orderid': orderid,
                'price': price,
                'return_url': return_url
            },
            'success': function (result) {
                if (result['code'] === 200) {
                    var key = result['data']['key'];
                    var keyInput = $("input[name='key']");
                    keyInput.val(key);
                    $("#pay-form").submit();
                }
            }
        });
    });
};

CourseOrder.prototype.run = function () {
    this.listenPayEvent();
};

$(function () {
    var courseOrder = new CourseOrder();
    courseOrder.run();
});