return do true false 3.5 -3 3.6778 -365.56 1 a

<script language="JavaScript">



<!-- Aqui se oculta el script a los visualizadores que no soportan JavaScript



// keep track of whether we just computed display.value

var computed = false



function pushStack(form)

{

    form.stack.value = form.display.value

    form.display.value = 0

}



//

// Define a function to add a new character to the display

//

function addChar(input, character)

{

    // auto-push the stack if the last value was computed

    if(computed) {

    pushStack(input.form)

    computed = false

    }



    // make sure input.value is a string

    if(input.value == null || input.value == "0")

        input.value = character

    else

        input.value += character

}



function deleteChar(input)

{

    input.value = input.value.substring(0, input.value.length - 1)

}



function add(form)

{

    form.display.value = parseFloat(form.stack.value)

                       + parseFloat(form.display.value)

    computed = true

}



function subtract(form)

{

    form.display.value = form.stack.value - form.display.value

    computed = true

}



function multiply(form)

{

    form.display.value = form.stack.value * form.display.value

    computed = true

}



function divide(form)

{

    var divisor = parseFloat(form.display.value)

    if(divisor == 0) {

    alert("Don't divide by zero, pal...");

    return

    }

    form.display.value = form.stack.value / divisor

    computed = true

}



function changeSign(input)

{

    // could use input.value = 0 - input.value, but let's show off substring

    if(input.value.substring(0, 1) == "-")

    input.value = input.value.substring(1, input.value.length)

    else

    input.value = "-" + input.value

}



<!-- done hiding from old browsers -->



</script>
