 const btn3 = document.getElementById('btn3');
                btn3.onclick = (e) => {
                    e.preventDefault();
                    var text = document.getElementById("acrotext").value;
                    if (text == ""){
                        alert("Вы находитесь на выборе первого слова!")
                        return
                    }
                    var myStringAsArray = text.split(" ");
                    console.log(myStringAsArray);
                    myStringAsArray.pop();
                    text = myStringAsArray[0];
                    for (i=1; i < myStringAsArray.length; i++ ){
                       text = text + " " + myStringAsArray[i];
                    }
                    var new_last_word = myStringAsArray[myStringAsArray.length - 1];
                    $("#acrotext").text(text);
                    $.ajax({
                        type: "POST",
                        url: '/ajax_del_word/',
                        data: {word: new_last_word},
                        success: function (msg) {
                            document.getElementById("select_word").options.length = 0;
                            for (i = 0; i < JSON.parse(msg)['words'].length; i++) {
                                document.getElementById("select_word").options[i] = new Option(JSON.parse(msg)['words'][i], "")
                            }
                        }
                    })
                };
    };