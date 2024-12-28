document.addEventListener("DOMContentLoaded", () => {
    const chatItems = document.querySelectorAll(".chat-item");
    const chatWindow = document.querySelector(".chat-window");
    const chatBody = document.querySelector(".chat-body");
    const messageInput = document.querySelector(".chat-footer input");
    const sendIcon = document.querySelector(".chat-footer .icon:last-child");
    const statusButton = document.getElementById("status-button");
    const ticketIdNumber = document.querySelector(".ticket-id-number");
    const ticketStatusContainer = document.querySelector(".ticket-id-container .ticket-status > div");
    let currentChatId = "";
    let chatHistory = {};

    // Function to add a message to the chat
    function addMessage(content, sent = true) {
        const messageContainer = document.createElement("div");
        const messageText = document.createElement("p");
        const frontCircle = document.createElement("div");
    
        // Set the class for the message container
        if (sent) {
            messageContainer.classList.add("sent-container");
            messageText.classList.add("sent");
            frontCircle.classList.add("front-circle-sent");
        } else {
            messageContainer.classList.add("received-container");
            messageText.classList.add("received");
            frontCircle.classList.add("front-circle-received");
        }
    
        // Set the message text content
        messageText.textContent = content;
    
        // Append the elements to the message container
        messageContainer.appendChild(messageText);
        messageContainer.appendChild(frontCircle);
    
        // Append the message container to the chat body
        chatBody.appendChild(messageContainer);
    
        // Scroll to the bottom of the chat body
        chatBody.scrollTop = chatBody.scrollHeight;
    
        // Update chat history
        if (!chatHistory[currentChatId]) {
            chatHistory[currentChatId] = [];
        }
        chatHistory[currentChatId].push({ content, sent });
    }

    // Event listener for sending message
    function sendMessage() {
        if (messageInput.value.trim() !== "") {
            addMessage(messageInput.value);
            messageInput.value = "";
        }
    }

    messageInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendMessage();
        }
    });

    sendIcon.addEventListener("click", sendMessage);

    // Event listener for switching chats
    chatItems.forEach(item => {
        item.addEventListener("click", () => {
            chatWindow.style.display = "block";
            chatBody.innerHTML = ""; // Clear chat window for demonstration
            currentChatId = item.querySelector(".chat-id").textContent.trim();
        
            // Update the ticketIdNumber element's text content
            ticketIdNumber.textContent = currentChatId;

            // Derive the chat history key
            const currentChatName = currentChatId;
            if (!chatHistory[currentChatName]) {
                chatHistory[currentChatName] = []; // Initialize chat history if it doesn't exist
            } else {
                // Populate chat history
                chatHistory[currentChatName].forEach(({ content, sent }) => {
                    addMessage(content, sent);
                });
            }

            // Update the status button and ticket status based on current chat status
            const currentStatusElement = item.querySelector(".ticket-status > div");
            const currentStatus = currentStatusElement.textContent.trim().toLowerCase();
            if (currentStatus === "open") {
                statusButton.classList.remove("open-status");
                statusButton.classList.add("close-status");
                statusButton.textContent = "Close Ticket";
            } else {
                statusButton.classList.remove("close-status");
                statusButton.classList.add("open-status");
                statusButton.textContent = "Open Ticket";
            }

            // Update the status in ticketIdContainer
            ticketStatusContainer.className = currentStatusElement.className;
            ticketStatusContainer.textContent = currentStatusElement.textContent;
        });
    });

    // Function to toggle the ticket status
    function toggleStatusBtn() {
        const currentStatus = ticketStatusContainer.textContent.trim().toLowerCase();
        if (currentStatus === "open") {
            ticketStatusContainer.textContent = "Closed";
            ticketStatusContainer.className = "purple-status";
            statusButton.classList.remove("close-status");
            statusButton.classList.add("open-status");
            statusButton.textContent = "Open Ticket";
        } else {
            ticketStatusContainer.textContent = "Open";
            ticketStatusContainer.className = "green-status";
            statusButton.classList.remove("open-status");
            statusButton.classList.add("close-status");
            statusButton.textContent = "Close Ticket";
        }

        // Update the status in the chat item
        const chatItem = Array.from(chatItems).find(item => item.querySelector(".chat-id").textContent.trim() === currentChatId);
        const chatItemStatus = chatItem.querySelector(".ticket-status > div");
        chatItemStatus.textContent = ticketStatusContainer.textContent;
        chatItemStatus.className = ticketStatusContainer.className;
    }

    statusButton.addEventListener("click", toggleStatusBtn);

    // Add event listeners for chat item click
    document.querySelectorAll('.chat-item').forEach(item => {
        item.addEventListener('click', function() {
            // Remove 'active' class from all chat items
            document.querySelectorAll('.chat-item').forEach(i => i.classList.remove('active'));
            // Add 'active' class to the clicked chat item
            this.classList.add('active');
        });
    });

    // Filter functionality
    const filterButtons = document.querySelectorAll(".filter-btn");
    filterButtons.forEach(button => {
        button.addEventListener("click", () => {
            // Remove active class from all buttons
            filterButtons.forEach(btn => btn.classList.remove("active"));
            // Add active class to the clicked button
            button.classList.add("active");
            const filter = button.getAttribute("data-filter");
            chatItems.forEach(item => {
                const status = item.querySelector(".ticket-status > div").textContent.toLowerCase();
                if (filter === "all" || status === filter) {
                    item.style.display = "";
                } else {
                    item.style.display = "none";
                }
            });
        });
    });
});
