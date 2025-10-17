import { initializeApp } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-auth.js";
import { getDatabase, ref, push, onValue, remove } from "https://www.gstatic.com/firebasejs/11.0.1/firebase-database.js";

import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyCBJBx6LkSsVCkUODyaUmKmgdwJxiQF_74",
  authDomain: "to-do-app-5a0ea.firebaseapp.com",
  databaseURL: "https://to-do-app-5a0ea-default-rtdb.firebaseio.com",
  projectId: "to-do-app-5a0ea",
  storageBucket: "to-do-app-5a0ea.firebasestorage.app",
  messagingSenderId: "1019073323053",
  appId: "1:1019073323053:web:bc8a7144884cc0a12458a4",
  measurementId: "G-L4N0GPGVXL"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getDatabase(app);

const email = document.getElementById("email");
const password = document.getElementById("password");
const signupBtn = document.getElementById("signupBtn");
const loginBtn = document.getElementById("loginBtn");
const logoutBtn = document.getElementById("logoutBtn");
const todoInput = document.getElementById("todoInput");
const addTodoBtn = document.getElementById("addTodoBtn");
const todoList = document.getElementById("todoList");
const todoSection = document.getElementById("todo-section");
const authSection = document.getElementById("auth-section");

signupBtn.addEventListener("click", () => {
  createUserWithEmailAndPassword(auth, email.value, password.value)
    .then(() => alert("Account created! Please login."))
    .catch(err => alert(err.message));
});

loginBtn.addEventListener("click", () => {
  signInWithEmailAndPassword(auth, email.value, password.value)
    .catch(err => alert(err.message));
});

logoutBtn.addEventListener("click", () => {
  signOut(auth);
});

onAuthStateChanged(auth, user => {
  if (user) {
    authSection.style.display = "none";
    todoSection.style.display = "block";
    logoutBtn.style.display = "inline";
    loadTodos(user.uid);
  } else {
    authSection.style.display = "block";
    todoSection.style.display = "none";
    logoutBtn.style.display = "none";
  }
});

addTodoBtn.addEventListener("click", () => {
  const user = auth.currentUser;
  if (user && todoInput.value.trim() !== "") {
    const todoRef = ref(db, "todos/" + user.uid);
    push(todoRef, { text: todoInput.value });
    todoInput.value = "";
  }
});

function loadTodos(uid) {
  const todoRef = ref(db, "todos/" + uid);
  onValue(todoRef, snapshot => {
    todoList.innerHTML = "";
    snapshot.forEach(child => {
      const li = document.createElement("li");
      li.textContent = child.val().text;
      const delBtn = document.createElement("button");
      delBtn.textContent = "❌";
      delBtn.onclick = () => remove(ref(db, "todos/" + uid + "/" + child.key));
      li.appendChild(delBtn);
      todoList.appendChild(li);
    });
  });
}
