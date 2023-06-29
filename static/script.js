// for navbar
function hideBar() {
    var bar = document.getElementById("baricon");
    var nav = document.getElementById("navig");
    bar.setAttribute("style", "display: none;");
    nav.classList.remove("hide");
}

function hideNav() {
    var bar = document.getElementById("baricon");
    var nav = document.getElementById("navig");
    bar.setAttribute("style", "display: block;");
    nav.classList.add("hide");
}

function toggleCommentarea() {
    var comment = document.getElementById("commentarea");
    var btn = document.getElementById("commentbtn");
    if (comment.style.display === "none") {
        comment.style.display = "block";
        btn.innerHTML = "Cancel";
    }
    else {
        comment.style.display = "none";
        btn.innerHTML = "Comment";
    }
}

function toggleReplyarea(id1, id2) {
    var reply = document.getElementById(id1);
    if (reply.style.display === "none") {
        reply.style.display = "block";
        var btn = document.getElementById(id2);
        btn.innerHTML = "Cancel";
    }
    else {
        reply.style.display = "none";
        var btn = document.getElementById(id2);
        btn.innerHTML = "Reply";
    }
}
