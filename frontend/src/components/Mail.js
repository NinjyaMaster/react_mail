import React from "react";
import { Link } from "react-router-dom";
import { useParams, useLocation } from "react-router-dom";

export default function Mail(props) {
  const { details } = props;
  const params = useParams();
  const location = useLocation();

  console.log(`json ${JSON.stringify(params)}`);
  console.log(`id ${params.id}`);
  console.log(`location : ${location.pathname}`);
  console.log(`location json : ${JSON.stringify(location)}`);

  //<div className="mail_id">{details.id}</div>

  return (
    <Link to={`${location.pathname}${details.id}/`}>
      <div className="mail">
        <div className="sender">{details.sender}</div>
        <div className="subject">{details.subject}</div>
      </div>
    </Link>
  );
}
