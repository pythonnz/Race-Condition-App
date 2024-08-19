var activateProblem = function(event, element) {
    event.preventDefault()
    let href = element.getAttribute("href")

    $.ajax({
        type: "POST",
        url: href,
        contentType: "application/json",
        success: function(response) {
            console.log(response)
        },
        error: function(xhr, status, error) {
            console.log(status, error)
        }
    })
}

var handleSubmit = function(event) {
    event.preventDefault();
    let challengeDiv = $(event.target).closest('.challenge');
    let challengeNumber = challengeDiv.data("challengenumber");
    let problemName = challengeDiv.data("problemname");

    console.log(challengeNumber)

    let answerInput = challengeDiv.find(".answer");
    let answer = answerInput.val();

    $.ajax({
        type: "POST",
        url: `/problems/${problemName}/challenges/${challengeNumber}/validate`,
        data: JSON.stringify({ data: answer }),
        contentType: 'application/json',
        success: function(response) {
            challengeDiv.removeClass("incorrect");
            challengeDiv.addClass("success");
            setTimeout(function () {
                $("#challenges-list").html(response.challenge_response);
                hljs.highlightAll();
            }, 1500);
        },
        error: function(xhr, status, error) {
            challengeDiv.removeClass("success");
            challengeDiv.addClass("incorrect");
        }
    });
}


$(document).ready(function(){

});
