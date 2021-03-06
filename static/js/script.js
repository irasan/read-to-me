// materialize components initialisation
$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.fixed-action-btn').floatingActionButton();
    $('.collapsible').collapsible();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
    $('.tooltipped').tooltip();

    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
  });

// validation for inputs that start with empty spaces 
document.getElementById("title").addEventListener('keydown', function (e) {
  if (this.value.length === 0 && e.which === 32) e.preventDefault();
});

document.getElementById("author").addEventListener('keydown', function (e) {
  if (this.value.length === 0 && e.which === 32) e.preventDefault();
});

document.getElementById("isbn").addEventListener('keydown', function (e) {
  if (this.value.length === 0 && e.which === 32) e.preventDefault();
});

document.getElementById("cover").addEventListener('keydown', function (e) {
  if (this.value.length === 0 && e.which === 32) e.preventDefault();
});

document.getElementById("query").addEventListener('keydown', function (e) {
  if (this.value.length === 0 && e.which === 32) e.preventDefault();
});