
        var dialogs = ["You know.", 
            "You know...the consequences.",
            "Even so...",
            "Could you do me a favor?",
            "Could you...",
            "Take care of them?",
            "Could you accept it?",
            "From now on...",
            "Everything that will happen."
        ]
        var dialogindex = 0;
        var index = 0
        var dialog = document.getElementById("dialog")
        dialog.innerText = "* " + dialogs[0]
        var password = new URLSearchParams(window.location.search).get('password')
        var music = new Audio('determination.mp3')
        if (password == "everythingthatwillhappen"){
            dialog.addEventListener("click", nextDialog)
            music.play()
            music.loop = true   
        } else if (password == "...")
            console.log("test")  
        } else {
            window.location.href="goodtry.html"
        }

        function nextDialog(){
            if (music.paused || music.ended || music.currentTime <= 0 ){
                music.play()
            }

            if (dialogindex + 1 < dialogs.length){
                index = 0
                dialogindex++
                dialog.innerText = "* "
            } else {
                window.location.href="determination.html"
            }
            typing()
        }

        function typing(){
            if (index < dialogs[dialogindex].length){
                dialog.innerText += dialogs[dialogindex].charAt(index)
                index++

                _time = 50
                
                if (dialog.innerText[index-1] == "."){
                    _time = 100
                }
                
                setTimeout(typing,_time)
            }
        }
