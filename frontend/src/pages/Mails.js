import React, { useEffect, useState } from "react";

import { useCookies } from "react-cookie";
import useAuthFetch from "../utls/useAuthFetch.js";
import Mail from "../components/Mail.js";
import { useParams, useLocation } from "react-router-dom";

export default function Mails(props) {
  const params = useParams();
  const location = useLocation();
  const { type, ...rest } = props;
  const [token] = useCookies(["mail-token"]);
  const [mails, setMails] = useState([]);

  //const [location, setLocation] = useState(useLocation());

  console.log(`json ${JSON.stringify(params)}`);
  console.log(`id ${params.id}`);
  console.log(`location : ${location.pathname}`);
  console.log(`location json : ${JSON.stringify(location)}`);

  const { get, post, loading } = useAuthFetch(
    "http://127.0.0.1:8000/",
    token["mail-token"]
  );

  useEffect(() => {
    let path = `api/mails/${type}/`;

    console.log(`path : ${path}`);
    if (token["mail-token"]) {
      //get("api/mails/")
      get(path)
        .then((data) => {
          //console.log(data);
          setMails(data);
        })
        .catch((error) => {
          console.log("Could not load mail list", error);
        });
    } else {
      window.location.href = "/";
    }
  }, [location]);

  return (
    <div>
      <h1 className="mailbox">{type}</h1>
      {mails.map((mail) => {
        return <Mail key={mail.id} details={mail} />;
      })}
    </div>
  );
}
