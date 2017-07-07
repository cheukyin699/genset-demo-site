/* global $, firebase, sessionID, usingFirebase */
var config = {
    apiKey: "AIzaSyBjM8SOL5rGiUq9gEF6NvBOMAWDO6Vfoqo",
    authDomain: "genset-demo-website.firebaseapp.com",
    databaseURL: "https://genset-demo-website.firebaseio.com",
    storageBucket: "genset-demo-website.appspot.com",
};
firebase.initializeApp(config);

function updateProgressbar(percent) {
    $(".progress-bar")
    .css("width", percent + "%")
    .attr("aria-valuenow", percent)
    .text(percent + "%");
}

function updateOutput(text) {
    $("#output").append(text + "<br>");

    if (text.includes("Warning")) {
        $(".progress-bar")
        .addClass("progress-bar-warning")
        .removeClass("progress-bar-success");
    } else if (text.includes("Error")) {
        $(".progress-bar")
        .addClass("progress-bar-danger")
        .removeClass("progress-bar-success progress-bar-warning");
    } else {
        $(".progress-bar")
        .addClass("progress-bar-primary")
        .removeClass("progress-bar-success progress-bar-warning progress-bar-danger");
    }
}

function deleteSession() {
    $.ajax({
        url: "/api/uploads/" + sessionID,
        type: "DELETE",
    })
    .done(function(resp) {
        window.location.href = "/";
    });
}

$(function() {
    if (usingFirebase) {
        var progressRef = firebase.database().ref("sessions/" + sessionID + "/progress");
        var textRef = firebase.database().ref("sessions/" + sessionID + "/text");
        textRef.on("value", function(snapshot) {
            // Add text to output
            updateOutput(snapshot.val());
        });
        progressRef.on("value", function(snapshot) {
            // Update progress bar
            updateProgressbar(snapshot.val());

            // If we get to 100, call everything off
            if (snapshot.val() >= 100) {
                progressRef.off("value");
                textRef.off("value");
            }
        });
    }

    $.ajaxSetup({
        cache: false
    });

    $.get("/api/uploads/" + sessionID + "/logs", function(data) {
        // Add original log text to output
        $("#output").html(data);
    });
});