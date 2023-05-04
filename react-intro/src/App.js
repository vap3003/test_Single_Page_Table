import './App.css';
import { useState, useEffect } from 'react';
import {Table, Container} from "reactstrap";

function App() {
  const [name, setName] = useState([]);


  useEffect(() => {
    names()
  }, [])

  const names = async () => {
    const responce = await fetch('http://127.0.0.1:8000/table/')
    setName(await responce.json())
  }

  return(
    <Container style={{marginTop: "50px"}}>
      <Table striped bordered hover variant="dark">
        <thead>
        <tr>
          <th>№</th>
          <th>Дата</th>
          <th>Название</th>
          <th>Количество</th>
          <th>Дистанция</th>
        </tr>
        </thead>
        <tbody>
        {name.map((data) => (
          <tr key={data.pk}>
            <td>{data.pk}</td>
            <td>{data.date}</td>
            <td>{data.name}</td>
            <td>{data.quantity}</td>
            <td>{data.distance}</td>
          </tr>
        )
        )}
        </tbody>
      </Table>
    </Container>
  )
}

export default App;
