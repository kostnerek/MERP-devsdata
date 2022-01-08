import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./containers/Navbar";
import Events from "./containers/Events";
import ManageReservation from "./containers/ManageReservation";

import "./styles/App.css";

function App() {
	return (
		<div className="App">
			<Router>
				<Navbar />
				<Routes>
					<Route exact path="/" element={<Events />}></Route>
					<Route exact path="/manage" element={<ManageReservation />}></Route>
				</Routes>
			</Router>
		</div>
	);
}

export default App;
