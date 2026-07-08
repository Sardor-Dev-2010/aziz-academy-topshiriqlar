// UI elementlarini aniqlab olamiz
const taskInput = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const list = document.getElementById('list');
const taskCounter = document.getElementById('taskCounter'); // Hisoblagich element

/**
 * Hisoblagich qiymatini yangilovchi funksiya.
 * 'ul' ichidagi 'li' elementlari sonini sanab, span'ga yozadi.
 */
function updateCounter() {
    const totalTasks = list.getElementsByTagName('li').length;
    taskCounter.textContent = totalTasks;
}

/**
 * Yangi vazifa qo'shish funksiyasi.
 */
function addTask() {
    const taskText = taskInput.value.trim();

    // Xatolikka chidamlilik: bo'sh kiritishni tekshirish
    if (taskText === "") {
        alert("Iltimos, vazifa matnini kiriting! ⚠️");
        return;
    }

    // Yangi 'li' elementi yaratish
    const li = document.createElement('li');
    
    // Matnni alohida 'span' ichiga olamiz
    const taskSpan = document.createElement('span');
    taskSpan.textContent = taskText;
    taskSpan.className = "task-text";
    
    // Vazifa matni bosilganda bajarilgan deb belgilash
    taskSpan.onclick = function() {
        taskSpan.classList.toggle('completed');
    };

    // O'chirish tugmasini yaratish
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = "O'chirish";
    deleteBtn.className = "delete-btn";
    
    // O'chirish hodisasi
    deleteBtn.onclick = function() {
        list.removeChild(li);
        updateCounter(); // Vazifa o'chirilganda hisoblagichni yangilash
    };

    // Elementlarni joylashtirish
    li.appendChild(taskSpan);
    li.appendChild(deleteBtn);
    list.appendChild(li);

    updateCounter(); // Yangi vazifa qo'shilganda hisoblagichni yangilash

    // Inputni tozalash va fokuslash
    taskInput.value = "";
    taskInput.focus();
}

// Hodisalarni tinglash (Event Listeners)
addBtn.addEventListener('click', addTask);

taskInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addTask();
    }
});
