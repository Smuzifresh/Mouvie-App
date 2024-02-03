let heart = $(".liked-mouvies svg")
console.log(heart)


function noname(like){
    $.ajax(`/films/like/${like}`, 
    {
        dataType: 'json', // type of response data
            
        success: function (data,status,xhr) {   // success callback function
            $(heart).parent().toggleClass("i-like-mouvie");
            console.log(data)
        },
        error: function (jqXhr, textStatus, errorMessage) { // error callback 
            console.log(errorMessage)
        }
    });
}

// noname()

$(heart).click(function (e) { 
    e.preventDefault();
    let filmId = $(this).data("filmid")
    noname(filmId)
    
   
});