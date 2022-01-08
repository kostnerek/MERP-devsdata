import { useState } from "react";

import "./../styles/ManageReservation.css";

const ManageReservation = () => {
  const [code, setCode] = useState("");
  const [message, setMessage] = useState("");

  const handleCancel = async () => {
    var myHeaders = new Headers();

    var requestOptions = {
      method: "PUT",
      headers: myHeaders,
      redirect: "follow",
    };

    // await fetch(`127.0.0.1:5000/reservation/KXOHOL`, requestOptions)
    await fetch(`http://127.0.0.1:5000/reservation/${code}`, requestOptions)
      .then((response) => response.json())
      .then((result) => {
        console.log(result);
        setMessage(result.message);
      })
      .catch((error) => console.log("error", error));
  };
  return (
    <div className="manage">
      <p>Input your registration code in order to manage your reservation.</p>
      <input
        type="text"
        placeholder="Input registration code"
        onChange={(e) => setCode(e.target.value)}
      ></input>
      <br></br>
      <br></br>
      <button onClick={(e) => handleCancel()}>Cancel reservation</button>
      <p>{message}</p>
    </div>
  );
};

export default ManageReservation;
