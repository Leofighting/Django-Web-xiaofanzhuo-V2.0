function PubCourse() {

}

PubCourse.prototype.initUEditor = function () {
    window.ue = UE.getEditor("editor", {
        "initialFrameHeight": 500,
        "serverUrl": "/ueditor/upload/"
    });

};

PubCourse.prototype.run = function () {
    this.initUEditor();
};

$(function () {
    var course = new PubCourse();
    course.run();
});