document.addEventListener('DOMContentLoaded', function() {
    const inputElements = document.querySelectorAll('.filter-panel input');

    function changeValue(element, labelElement) {
        let value = labelElement.nextElementSibling;
        value.textContent = element.value;
    }

    inputElements.forEach(element => {
        let labelElement = document.querySelector(`label[for='${element.id}']`);
        if (labelElement) {
            labelElement.insertAdjacentHTML('afterend', `<span>${element.value}</span>`);
            element.addEventListener('change', () => changeValue(element, labelElement));
        }
    });
});
