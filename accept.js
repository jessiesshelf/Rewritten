
        var dialogs = ["You know.", "You know...the consequences.","Even so...","Could you accept it?","From now on...","Everything that will happen."]
        var dialogindex = 0;
        var index = 0
        var dialog = document.getElementById("dialog")
        dialog.innerText = "* " + dialogs[0]
        var password = new URLSearchParams(window.location.search).get('password')
        if (password == "everythingthatwillhappen"){
            dialog.addEventListener("click", nextDialog)
            music = new Audio('determination.mp3')
            music.play()
            music.loop = true
        } else if (password == "") {
            dialog.addEventListener("click", window.location.href="goodtry.html")
        }

        function nextDialog(){
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
                setTimeout(typing,50)
            }
        }