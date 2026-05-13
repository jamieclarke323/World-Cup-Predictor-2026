const buttons = document.querySelectorAll(
    '.prediction-button'
);

buttons.forEach(button => {

    button.addEventListener('click', function() {

        const parent =
            this.parentElement;

        parent.querySelectorAll(
            '.prediction-button'
        ).forEach(btn => {

            btn.classList.remove(
                'selected'
            );

        });

        this.classList.add(
            'selected'
        );

        const fixtureId =
            this.dataset.fixture;

        const prediction =
            this.dataset.prediction;

        fetch('/save-prediction', {

            method: 'POST',

            headers: {
                'Content-Type':
                    'application/x-www-form-urlencoded'
            },

            body:
                `fixture_id=${fixtureId}&prediction=${prediction}`

        })

        .then(response => response.text())

        .then(data => {

            console.log(data);

        });

    });

});