const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			genres: [],
		},
		actions: {
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			getMessage: async () => {
				try {
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				} catch (error) {
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			},
				// Get Genres for lists
			// loadGenres: async () => {
			// 	try {
			// 		const options = { method: 'GET', headers: {} };
			// 		const response = await fetch("https://api.deezer.com/genre", options)
			// 		if (!response.ok) {
			// 			console.error("Fetch error loadGenres")
			// 		}
			// 		const data = await response.json()
			// 		setStore({ genres: data["name", "picture"] })
			// 	}
			// 	catch (error) {
			// 		console.error("Failed to load genres")
			// 	}
			// },

		}
	};
};

export default getState;
