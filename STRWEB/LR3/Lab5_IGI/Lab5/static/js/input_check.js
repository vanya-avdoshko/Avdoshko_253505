document.addEventListener("DOMContentLoaded", function () {
    const emailInput = document.getElementById("id_email"); 
    const phoneInput = document.getElementById("id_phone");
    const submitButton = document.getElementById("btn-form-disabled");
    const emailTooltip = document.getElementById("emailTooltip");
    const phoneTooltip = document.getElementById("phoneTooltip");

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const phoneRegex = /^(8|\+?375)\s*(\(?\d{2,3}\)?)\s?\d{3}[\s-]?\d{2}[\s-]?\d{2}$/;

    const validateField = (input, regex, tooltip) => {
        const value = input.value.trim();
        if (!regex.test(value)) {
            input.classList.add("form-invalid");
            tooltip.style.display = "inline";
            return false;
        } else {
            input.classList.remove("form-invalid");
            tooltip.style.display = "none";
            return true;
        }
    };

    const validateForm = () => {
        const isEmailValid = validateField(emailInput, emailRegex, emailTooltip);
        const isPhoneValid = validateField(phoneInput, phoneRegex, phoneTooltip);
        return isEmailValid && isPhoneValid;
    };

    submitButton.addEventListener("click", function (event) {
        event.preventDefault(); 
        if (validateForm()) {
            document.querySelector("form").submit(); 
        }
    });

    emailInput.addEventListener("input", function() {
        validateField(emailInput, emailRegex, emailTooltip);
    });

    phoneInput.addEventListener("input", function() {
        validateField(phoneInput, phoneRegex, phoneTooltip);
    });
});
