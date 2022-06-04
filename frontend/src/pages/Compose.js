import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar.js";
import { useParams, useLocation } from "react-router-dom";
import useAuthFetch from "../utls/useAuthFetch.js";
import { useCookies } from "react-cookie";

export default function Compose() {
  const [recipientsStr, setRecipientsStr] = useState("");
  const [subject, setSubject] = useState("");
  const [body, setBody] = useState("");
  const [token] = useCookies(["mail-token"]);

  const { post, loading } = useAuthFetch(
    "http://127.0.0.1:8000/",
    token["mail-token"]
  );

  function handleFormSubmit(event) {
    event.preventDefault();
    const recipients = convertToRecipients(recipientsStr);
    post("api/send/", { recipients, subject, body })
      .then((data) => {
        console.log(data);
        window.location.href = "/mail/inbox/";
      })
      .catch((error) => console.log(error));
  }

  function convertToRecipients(str) {
    const tmp = [];
    tmp.push(str);
    return tmp;
  }

  return (
    <div>
      <h1 className="mailbox">New Message</h1>
      <form onSubmit={handleFormSubmit}>
        <input
          id="recipients"
          type="text"
          placeholder="Recipients"
          value={recipientsStr}
          onChange={(evt) => setRecipientsStr(evt.target.value)}
          className="form-textinput"
        />
        <br></br>
        <input
          id="subject"
          type="text"
          placeholder="Subject"
          value={subject}
          onChange={(evt) => setSubject(evt.target.value)}
          className="form-textinput"
        />
        <br></br>
        <textarea
          id="body"
          type="text"
          value={body}
          onChange={(evt) => setBody(evt.target.value)}
          className="form-textarea"
        />
        <br></br>
        <input type="submit" value="Send" className="buttonInactive" />
      </form>
    </div>
  );
}
