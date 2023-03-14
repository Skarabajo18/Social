import React, { useState } from 'react';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = { email: email, password: password };

    fetch('http://localhost:8000/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email:
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label>
      <br />
      <button type="submit">Login</button>
    </form>
  );
}

export default Login;




































// import Button from 'react-bootstrap/Button';
// import Form from 'react-bootstrap/Form';

// function Login() {
//   return (
//     <Form>
//       <Form.Group className="mb-3" controlId="formBasicEmail">
//         <Form.Label>Correo</Form.Label>
//         <Form.Control type="email" placeholder="Ingresa correo" />
//         <Form.Text className="text-muted">
//         <Form.Control.Feedback />
//           Nunca compartiremos tu informacion con terceros.
//         </Form.Text>
        
//       </Form.Group>

//       <Form.Group className="mb-3" controlId="formBasicPassword">
//         <Form.Label>Contraseña</Form.Label>
//         <Form.Control type="password" placeholder="Ingresa una contraseña" />
//       </Form.Group>
//       <Button variant="primary" type="submit">
//         Ingresar
//       </Button>
//     </Form>
//   );
// }

// export default Login;
