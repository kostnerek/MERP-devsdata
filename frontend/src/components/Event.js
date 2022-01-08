import { useState } from "react";
import Modal from "../Modal";

const Event = (props) => {
	const [showModal, setShowModal] = useState(false);
	const [eventCode, setEventCode] = useState("");

	const toggleModal = () => {
		setShowModal(!showModal);
	};

	const handleRegister = async () => {
		var myHeaders = new Headers();
		myHeaders.append("Content-Type", "application/json");

		var raw = JSON.stringify({
			title: props.title,
		});

		var requestOptions = {
			method: "POST",
			headers: myHeaders,
			body: raw,
			redirect: "follow",
		};

		const res = await fetch(
			"http://127.0.0.1:5000/reservation/create",
			requestOptions
		)
			.then((response) => response.json())
			.then((result) => {
				console.log(result);
				setEventCode(result.code);
				toggleModal();
			})
			.catch((error) => console.log("error", error));
	};

	return (
		<div className="events-event">
			<div className="events-event-thumbnail">
				<img src={`${props.thumbnail}`} alt="event thumbnail" />
			</div>
			<div className="events-event-title">{props.title}</div>
			<div className="events-event-start">start: {props.startDate}</div>
			<div className="events-event-end">stop: {props.endDate}</div>
			<div className="events-event-register">
				<button
					onClick={() => {
						handleRegister();
					}}
				>
					Register
				</button>
			</div>
			{showModal ? (
				<Modal>
					<div onClick={() => toggleModal()}>
						<div>Your reservation code is: {eventCode}</div>
						<div className="modal-reservation-code"></div>
					</div>
				</Modal>
			) : null}
		</div>
	);
};

export default Event;
