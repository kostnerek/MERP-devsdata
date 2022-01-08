import { useState, useEffect } from "react";

import Event from "../components/Event";

import "./../styles/Events.css";

const Events = () => {
  const [events, setEvents] = useState({
    eventsState: "loading",
    events: [
      {
        thumbnail: "",
        title: "",
        startDate: "",
        endDate: "",
      },
    ],
  });

  useEffect(async () => {
    var requestOptions = {
      method: "GET",
      redirect: "follow",
    };

    await fetch("http://127.0.0.1:5000/event", requestOptions)
      .then((response) => response.json())
      .then((result) => {
        setEvents({ eventsState: "loaded", events: result.events });
      })
      .catch((error) => console.log("error", error));
  }, []);

  return (
    <div className="events">
      {events.eventsState === "loading" ? (
        <div className="events-message">Loading events...</div>
      ) : (
        events.events.map((event) => {
          let start = new Date(event.startDate);
          let end = new Date(event.endDate);
          return (
            <Event
              thumbnail={event.thumbnail}
              title={event.title}
              startDate={start.toLocaleDateString({
                year: "numeric",
                month: "numeric",
                day: "numeric",
              })}
              endDate={end.toLocaleDateString({
                year: "numeric",
                month: "numeric",
                day: "numeric",
              })}
              key={event.title}
            />
          );
        })
      )}
    </div>
  );
};

export default Events;
