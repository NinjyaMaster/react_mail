import React from "react";
//import clsx from "clsx";

export default function Button(props) {
  //const { children, outline, className, ...rest } = props;
  const { children, ...rest } = props;

  // const classNames = clsx({
  //     btn: true,
  //     "btn-default": !outline,
  //     "btn-outline": outline,
  //   },
  //   className
  // );
  //<button className={classNames} {...rest}>

  return <button {...rest}>{children}</button>;
}
