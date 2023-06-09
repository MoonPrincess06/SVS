/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './SVS/templates/**/*.{html,js}',
        './teachers/templates/**/*.{html,js}',
        './students/templates/**/*.{html,js}',
        './lessons/templates/**/*.{html,js}',
    ],
    theme: {
        extend: {
            colors: {
                accent: {
                    50: "rgba(255, 109, 112, 0.83)",
                    100: "#ff6f61",
                },
                primary: {
                    900: '#002942',
                    800: '#003250',
                    700: '#003a5d',
                    DEFAULT: "#00426a",
                    600: '#205a7d',
                    500: '#40718f',
                    400: '#6089a2',
                    300: '#80a1b4',
                    200: '#9fb8c7',
                    100: '#bfd0da',
                    50: 'rgba(223,231,237,0.5)'

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


