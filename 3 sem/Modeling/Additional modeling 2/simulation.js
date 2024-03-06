var connectionType = 'sequential';

document.getElementById('sequential').addEventListener('click', function() {
    createSpringInputs(5);
    connectionType = 'sequential';
    updateConnectionTypeDisplay();
});

document.getElementById('parallel').addEventListener('click', function() {
    createSpringInputs(5);
    connectionType = 'parallel';
    updateConnectionTypeDisplay();
});

document.getElementById('toggle').addEventListener('click', function() {
    if (connectionType === 'sequential') {
        connectionType = 'parallel';
    } else {
        connectionType = 'sequential';
    }
    createSpringInputs(5);
    updateConnectionTypeDisplay();
});



document.getElementById('calculate').addEventListener('click', function() {
    var k_values = [];
    var springs = document.getElementsByClassName('spring');
    for (var i = 0; i < springs.length; i++) {
        var k_value = parseFloat(springs[i].value);
        if (!isNaN(k_value)){
            k_values.push(k_value);
        }
    }

    if (k_values.length === 0){
        alert("Вы не ввели ни одного значения коэффициента жёсткости")
        return;
    }

    var checker = false;

    var displacement = parseFloat(document.getElementById('displacement').value);
    var inputforce = parseFloat(document.getElementById('force').value);
    var dis = calculateDisplacement(k_values, inputforce)
    if (isNaN(displacement) && isNaN(inputforce)) {
        alert("Пожалуйста введите либо значение силы, либо значение сжатия")
        return;
    }

    if (!isNaN(displacement) && !isNaN(inputforce)) {
        alert("Пожалуйста введите только одно из этих двух значений")
        return;
    }

    var force = calculateForce(k_values, displacement);
    var K = calculateK(k_values);
    if (isNaN(displacement)) {
        document.getElementById('result').innerText = 'Сжатие ' + dis.toFixed(2) + ' м';
    }else{
        document.getElementById('result').innerText = 'Сила: ' + force.toFixed(2) + ' Н';
    }
    document.getElementById("K").innerHTML = "k<sub>эффективная</sub>" + ": " + K.toFixed(2) + " Н/м";

    drawSprings(k_values, displacement);
});

function createSpringInputs(n) {
    var container = document.getElementById('springs');
    container.innerHTML = '';
    for (var i = 0; i < n; i++) {
        var input = document.createElement('input');
        input.type = 'number';
        input.className = 'spring';
        input.placeholder = 'k' + (i + 1) + ' (Н/м)';
        container.appendChild(input);
    }

    var separator = document.createElement('p');
    separator.innerText = 'Если вы введете значение силы, то результатом будет значение смещения,' +
        ' а если введете значение смещения, то результатом будет значение силы';
    container.appendChild(separator);

    var displacement = document.createElement('input');
    displacement.type = 'number';
    displacement.id = 'displacement';
    displacement.placeholder = 'Смещение (м)';
    container.appendChild(displacement);

    var inputforce = document.createElement('input');
    inputforce.type = 'number';
    inputforce.id = 'force';
    inputforce.placeholder = 'Сила (Н)';
    container.appendChild(inputforce);
}

function calculateForce(k_values, displacement) {
    var k_total;
    if (connectionType === 'sequential') {
        var k_inverse_sum = 0;
        for (var i = 0; i < k_values.length; i++) {
            k_inverse_sum += 1 / k_values[i];
        }
        k_total = 1 / k_inverse_sum;
        K = k_total;
    } else {
        var k_sum = 0;
        for (var i = 0; i < k_values.length; i++) {
            k_sum += k_values[i];
        }
        k_total = k_sum;
        K = k_total;
    }
    var force = k_total * displacement;
    return force;
}

function calculateK(k_values) {
    var k_total;
    if (connectionType === 'sequential') {
        var k_inverse_sum = 0;
        for (var i = 0; i < k_values.length; i++) {
            k_inverse_sum += 1 / k_values[i];
        }
        k_total = 1 / k_inverse_sum;
    } else {
        var k_sum = 0;
        for (var i = 0; i < k_values.length; i++) {
            k_sum += k_values[i];
        }
        k_total = k_sum;
    }
    return k_total;
}

function calculateDisplacement(k_values, force) {
    var k_total;
    if (connectionType === 'sequential') {
        var k_inverse_sum = 0;
        for (var i = 0; i < k_values.length; i++) {
            k_inverse_sum += 1 / k_values[i];
        }
        k_total = 1 / k_inverse_sum;
    } else {
        var k_sum = 0;
        for (var i = 0; i < k_values.length; i++) {
            k_sum += k_values[i];
        }
        k_total = k_sum;
    }
    var displacement = force / k_total;
    return displacement;
}


function updateConnectionTypeDisplay() {
    var display = document.getElementById('connectionTypeDisplay');
    display.innerText = 'Текущий тип подключения: ' + (connectionType === 'sequential' ? 'Последовательное' : 'Параллельное');
}


function drawSprings(k_values) {
    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  
    var amplitude = 10; // Амплитуда волны
    var frequency = 241 % 10; // Частота волны
    var phase = 1000;
    if (connectionType === 'sequential') {
        ctx.beginPath();
        for (var x = 0; x < canvas.width; x ++) {
            var y = amplitude * Math.sin((x + phase) * frequency) + canvas.height / 2;
            ctx.lineTo(x + k_values.length, y);
        }
        ctx.stroke();
        anime({
            targets: canvas,
            scaleX: {
                value: [1, ((241 * 0.3)) % 0.5, 1],
                duration: 800,
                easing: 'easeInQuad',
                complete: function(anim) {
                    canvas.style.transform = '';
                }
            }
        });
    } else {
        for (var i = 0; i < k_values.length; i++) {
            ctx.beginPath();
            for (var x = 0; x < canvas.width; x++) {
                var y = amplitude * Math.sin((x + phase + i * Math.PI / 2) * frequency) + canvas.height / 2;
                y += i * 50;
                ctx.lineTo(y, x);
            }
            ctx.stroke();
            anime({
                targets: canvas,
                scaleY: {
                    value: [1, ((241 * 0.3)) % 0.5, 1],
                    duration: 800,
                    easing: 'easeInQuad',
                    complete: function(anim) {
                        canvas.style.transform = '';
                    }
                }
            });
        }
    }
}
