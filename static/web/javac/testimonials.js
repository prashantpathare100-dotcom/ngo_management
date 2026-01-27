function filterSelection(c) {
            var x, i;
            x = document.getElementsByClassName("filter-item");
            
            // Remove active class from buttons
            var btns = document.getElementsByClassName("filter-btn");
            for (i = 0; i < btns.length; i++) {
                btns[i].classList.remove("active");
            }
            // Add active to clicked button (find by text content roughly)
            event.target.classList.add("active");

            if (c == "all") c = "";
            
            for (i = 0; i < x.length; i++) {
                x[i].style.display = "none";
                x[i].classList.remove("item-show");
                
                if (x[i].className.indexOf(c) > -1) {
                    x[i].style.display = "block";
                    setTimeout(() => x[i].classList.add("item-show"), 50)
                }
            }
        }