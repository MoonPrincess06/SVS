/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './SVS/templates/**/*.{html,js}'
    ],
    theme: {
        extend: {
            colors: {
                accent: {
                    50: "rgba(255, 109, 112, 0.83)",
                    100: "#ff6f61",
                },
                primary: {
                    100: "#00426a",
                }
            },
        },
        fontFamily: {
            'serif': [
                'EB Garamond',

            ],
            'sans': [
                'Barlow',
            ]
        }
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
    ],
}


