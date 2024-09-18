/** @type {import('tailwindcss').Config} */
module.exports = {
	darkMode: "media",
	content: [
		'./templates/**/*.html'
	],
	theme: {
		extend: {
			fontFamily: {
				prompt: ["Prompt"],
				mitr: ["Mitr"],
				bungee: ["Bungee+Tint"],
			},
			animation: {
				'slide-up': 'slideUp 0.8s ease-out',
				'fade-in-up': 'fade-in-up 0.5s ease-out forwards',
			},
			keyframes: {
				slideUp: {
				  '0%': {
					opacity: '0',
					transform: 'translateY(50px)'
				  },
				  '100%': {
					opacity: '1',
					transform: 'translateY(0)'
				  }
				},
				'fade-in-up': {
				  '0%': { opacity: '0', transform: 'translateY(20px)' },
				  '100%': { opacity: '1', transform: 'translateY(0)' },
				},
				
			},
		},
	},
	plugins: [],
}
