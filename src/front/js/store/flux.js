
const API_URL = process.env.BACKEND_URL

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
			]
		},
		actions: {
			// Use getActions to call a function within a fuction
			createNewPatient: async (newPatient) => {
				try {
					const response = await fetch(API_URL + "/api/signup_patient", {
						method: "POST",
						body: JSON.stringify(newPatient),
						headers: {
							"Content-Type": "application/json"
						}

					});
					if (!response.ok) {
						throw new Error("There was a problem with the funtion in flux")
					}
					const data = await response.json();
					console.log("User created successfully", data)


				} catch (error) {
					console.error("There was an error tryinig to create the Patient", error)
				}
			},

			createNewSpecialist: async (newSpecialist) => {
				try {
					const response = await fetch(API_URL + "/api/signup_specialist", {
						method: "POST",
						body: JSON.stringify(newSpecialist),
						headers: {
							"Content-Type": "application/json"
						}

					});
					if (!response.ok) {
						throw new Error("There was a problem with the funtion in flux")
					}
					const data = await response.json();
					console.log("User created successfully", data)


				} catch (error) {
					console.error("There was an error tryinig to create the Specialist", error)
				}
			},


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
			}
		}
	};
};

export default getState;
