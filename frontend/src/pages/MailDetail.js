import React, { useEffect, useState } from "react";
import { useParams, useLocation } from "react-router-dom";
import useAuthFetch from "../utls/useAuthFetch.js";
import { useCookies } from "react-cookie";
import Navbar from "../components/Navbar.js";
import Button from "../components/Button.js";

export default function MailDetail() {
  const [token] = useCookies(["mail-token"]);
  const [mail, setMail] = useState({});
  const params = useParams();
  //const { id } = useParams(); // this works too

  const { get, remove, put, loading } = useAuthFetch(
    "http://127.0.0.1:8000/",
    token["mail-token"]
  );

  //const location = useLocation();

  //   console.log(`json ${JSON.stringify(params)}`);
  //   console.log(`id ${params.id}`);
  //   console.log(`location : ${location.pathname}`);
  //   console.log(`location json : ${JSON.stringify(location)}`);

  useEffect(() => {
    get(`api/mail/${params.id}/`)
      .then((data) => {
        console.log(data);
        setMail(data);
      })
      .catch((error) => {
        console.log(`something is wrong ${error}`);
      });
  }, []);

  function handleDeleteClick() {
    remove(`api/mail/${params.id}/`)
      .then((data) => {
        console.log(data);
        window.location.href = "/mail/inbox/";
      })
      .catch((error) => {
        console.log(`something is wrong ${error}`);
      });
  }

  function handleArchiveClick() {
    const newMail = { ...mail, archived: true };
    put(`api/mail/${params.id}/`, newMail)
      .then((data) => {
        console.log(data);
        window.location.href = "/mail/inbox/";
      })
      .catch((error) => {
        console.log(`something is wrong ${error}`);
      });
  }

  return (
    <div className="mailDetail">
      <h1 className="subject">{mail.subject}</h1>
      <div className="senderInfo">
        <p className="sender">{mail.sender}</p>
        <p className="timestamp">{mail.timestamp}</p>
      </div>
      <p className="body">{mail.body}</p>
      <Button className="buttonInactive" onClick={handleDeleteClick}>
        Delete
      </Button>
      <Button onClick={handleArchiveClick} className="buttonInactive">
        Archive
      </Button>
    </div>
  );
}
