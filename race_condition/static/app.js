
$(document).ready(function(){
    $("#challengeSubmitButton").click(function(event){
        event.preventDefault(); // Prevent default action of the link
        let answer = $("#answer").val()
        let challengeNumber = $("#challenge").data("challengenumber")
        let problemName = $("#challenge").data("problemname")

        $.ajax({
            type: "POST",
            url: `/problems/${problemName}/challenges/${challengeNumber}/validate`,
            data: JSON.stringify({ data: answer }),
            contentType: 'application/json',
            success: function(response) {
                $("#challenge").outerHTML("success", response.json())
                console.log(response); // Handle the response here
            },
            error: function(xhr, status, error) {
                // $("#challenge").outerHTML("success", response.json()
                console.error(error); // Handle errors here
            }
        });
    });
});

