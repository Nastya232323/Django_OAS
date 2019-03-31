document.addEventListener('keydown', function (e) {
    const s = document.getElementById("select_word");
    if (e.keyCode === 49){
        e.preventDefault();
        let index_of_word = 0;
        if ($(e.target).closest("#number_input").length == 1){
            document.getElementById("number_input").value = document.getElementById("number_input").value + "1";
            return;
        }
        $.ajax({
            async: false,
            type: "POST",
            url: '/ajax/',
            data: $('#Text'),
            success: function (msg) {
                $("#acrotext").text("");
                for (let i = 0; i < JSON.parse(msg)['words'].length; i++) {
                    document.getElementById("select_word").options[i] = new Option(i + "   " + JSON.parse(msg)['words'][i], i)
                };
                $("#select_word :first").attr("selected", "selected");
            }
        });
        for (let number = 0; number < 4; number++) {
            let word = s.options[index_of_word + number].text;
            word = word.split(" ")[1];
            $.ajax({
                type: "POST",
                url: '/get_top_five_words/',
                data: {word: word},
                success: function (msg) {
                    console.log(JSON.parse(msg)['words']);
                    document.getElementById("Label" + (number + 1)).textContent = "Для " + (index_of_word + number) + "-ого слова";
                    for (let i = 0; i < 5; i++) {
                        if (i < JSON.parse(msg)['words'].length){
                            document.getElementById("li" + (i + 1 + number * 5)).text = JSON.parse(msg)['words'][i];
                        }
                        else {
                            document.getElementById("li" + (i + 1 + number * 5)).text = "";
                        }
                    }
                }
            })
        }
    }
    if (e.keyCode === 40) {
        e.preventDefault();
        const current_word = s.options.selectedIndex;
        if (current_word == s.options.length - 1) {
            return;
        }
        s.options[current_word + 1].selected = true;
        const selectTop = $(s).offset().top;
        const optionTop = $(s).find('option:selected').offset().top;
        let index_of_word = s.options.selectedIndex;
        if (s.options.selectedIndex + 4 >= s.options.length) {
            index_of_word = s.options.length - 4;
        }
        for (let number = 0; number < 4; number++) {
            let word = s.options[index_of_word + number].text;
            word = word.split(" ")[1];
            console.log(word);
            $.ajax({
                type: "POST",
                url: '/get_top_five_words/',
                data: {word: word},
                success: function (msg) {
                    console.log(JSON.parse(msg)['words']);
                    document.getElementById("Label" + (number + 1)).textContent = "Для " + (index_of_word + number) + "-ого слова";
                    for (let i = 0; i < 5; i++) {
                        if (i < JSON.parse(msg)['words'].length){
                            document.getElementById("li" + (i + 1 + number * 5)).text = JSON.parse(msg)['words'][i];
                        }
                        else {
                            document.getElementById("li" + (i + 1 + number * 5)).text = "";
                        };
                    };
                }
            });
        };
        $(s).animate({scrollTop: $(s).scrollTop() + (optionTop - selectTop)}, 200);
    };
    if (e.keyCode === 53) {
        e.preventDefault();
        if ($(e.target).closest("#number_input").length == 1){
            document.getElementById("number_input").value = document.getElementById("number_input").value + "5";
            return;
        }
        const s = document.getElementById("select_word");
        const current_word = s.options.selectedIndex;
        if (current_word + 5 >= s.options.length){
            return;
        }
        const selectTop = $(s).offset().top;
        const optionTop = $(s.options[current_word + 5]).offset().top;
        $(s).animate({scrollTop: $(s).scrollTop() + (optionTop - selectTop)}, 400);
        s.options[current_word + 5].selected = true;
    };
    if (e.keyCode == 38){
        e.preventDefault();
        const s = document.getElementById("select_word");
        const current_word = s.options.selectedIndex;
        if (current_word == 0){
            return;
        }
        const selectTop = $(s).offset().top;
        const optionTop = $(s.options[current_word]).prev().offset().top;
        $(s).animate({scrollTop: $(s).scrollTop() + (optionTop - selectTop)}, 200);
        s.options[current_word - 1].selected = true;
    }
    if (e.keyCode === 54) {
        e.preventDefault();
        if ($(e.target).closest("#number_input").length == 1){
            document.getElementById("number_input").value = document.getElementById("number_input").value + "6";
            return;
        }
        const s = document.getElementById("select_word");
        const current_word = s.options.selectedIndex;
        if (current_word - 5 < 0){
            return;
        }
        const selectTop = $(s).offset().top;
        const optionTop = $(s.options[current_word - 5]).offset().top;
        $(s).animate({scrollTop: $(s).scrollTop() + (optionTop - selectTop)}, 400);
        s.options[current_word - 5].selected = true;
    };
    if (e.keyCode == 32){
       if ($(e.target).closest("#number_input").length == 1) {
           const index = document.getElementById("number_input").value;
           s.options[index].selected = true;
           let new_word = s.options[index].text;
           let text = document.getElementById("acrotext").value;
           new_word = new_word.split(" ")[1];
           document.getElementById("number_input").value = "";
           $.ajax({
               type: "POST",
               url: '/ajax_words/',
               data: {word: new_word},
               success: function (msg) {
                   s.options.length = 0;
                   if (JSON.parse(msg)['message'] == "Ok") {
                       text = text + " " + new_word;
                   }
                   else if (JSON.parse(msg)['message'] == "Вы сгенерировали Ваш акротекст") {
                       text = text + " " + new_word;
                       $("#acrotext").text(text);
                       alert(JSON.parse(msg)['message']);
                   }
                   else {
                       alert(JSON.parse(msg)['message']);
                   };
                   for (i = 0; i < JSON.parse(msg)['words'].length; i++) {
                       document.getElementById("acrotext").clear;
                       s.options[i] = new Option(i + " " + JSON.parse(msg)['words'][i], i);
                       s.options[0].selected = true;
                   };
                   $("#acrotext").text(text);
               }
           })
       }
    };
})