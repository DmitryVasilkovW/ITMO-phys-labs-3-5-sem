const c = 299792458;

function calculate() {
    const V = parseFloat(document.getElementById('V').value);
    const v_prime = parseFloat(document.getElementById('v_prime').value);
    const x_prime = parseFloat(document.getElementById('x_prime').value);
    const t_prime = parseFloat(document.getElementById('t_prime').value);

    if (isNaN(V)) {
        alert("Пожалуйста, введите значение для скорости системы отсчета V (м/с).");
        return;
    }

    if (isNaN(v_prime)) {
        alert("Пожалуйста, введите значение для скорости материальной точки v' (м/с).");
        return;
    }

    if (isNaN(x_prime)) {
        alert("Пожалуйста, введите значение для начальной координаты материальной точки x₀' (м).");
        return;
    }

    if (isNaN(t_prime)) {
        alert("Пожалуйста, введите значение для времени t (с).");
        return;
    }

    if (V >= c || v_prime >= c) {
        alert("Введенные значения не должны быть релятивистскими.");
        return;
    }

    const v = V + v_prime;
    const x = x_prime + v * t_prime;
    const t = t_prime;

    document.getElementById('output').innerHTML = 'Скорость v: ' + v.toFixed(2) + ' м/с, Координата x: ' + x.toFixed(2) + ' м, Время t: ' + t.toFixed(2) + ' с';
}

function calculatePrime() {
    const V = parseFloat(document.getElementById('V2').value);
    const v = parseFloat(document.getElementById('v').value);
    const x = parseFloat(document.getElementById('x').value);
    const t = parseFloat(document.getElementById('t').value);

    if (isNaN(V)) {
        alert("Пожалуйста, введите значение для скорости системы отсчета V (м/с).");
        return;
    }

    if (isNaN(v)) {
        alert("Пожалуйста, введите значение для скорости материальной точки v (м/с).");
        return;
    }

    if (isNaN(x)) {
        alert("Пожалуйста, введите значение для координататы материальной точки x (м).");
        return;
    }

    if (isNaN(t)) {
        alert("Пожалуйста, введите значение для времени t (с).");
        return;
    }

    if (V >= c || v >= c) {
        alert("Введенные значения не должны быть релятивистскими.");
        return;
    }

    const v_prime = v - V;
    const x_prime = x - v * t;
    const t_prime = t;

    document.getElementById('output').innerHTML = "Скорость v': " + v_prime.toFixed(2) + " м/с, Координата x<sub>0</sub>': " + x_prime.toFixed(2) + " м, Время t: " + t_prime.toFixed(2) + " с";
}
