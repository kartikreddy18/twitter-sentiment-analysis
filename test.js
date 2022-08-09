import fetch from "node-fetch";

const sentiment = async (data) => {
  console.log(data);
  const response = await fetch("http://localhost:8000/predict", {
    method: "post",
    mode: "no-cors",
    headers: {
      "Content-Type": "application/json",
    },
    body: data,
  });
  console.log(response.status);
  console.log(response.statusText);
  console.log(await response.json());
};

const data = JSON.stringify({
  text: "I am happy",
});

sentiment(data);
