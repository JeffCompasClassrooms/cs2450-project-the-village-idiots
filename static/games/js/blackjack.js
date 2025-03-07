document.addEventListener('DOMContentLoaded', () => {
	// Global variables for game state
	let deck = [];
	let playerHand = [];
	let dealerHand = [];
	let gameOver = false;
	let playerStands = false;

	// Get DOM elements
	const dealButton = document.getElementById('deal-button');
	const hitButton = document.getElementById('hit-button');
	const standButton = document.getElementById('stand-button');
	const playerHandDiv = document.querySelector('#player-hand .hand');
	const dealerHandDiv = document.querySelector('#dealer-hand .hand');

	// Create or get message element to display game status
	let gameMessageDiv = document.getElementById('game-message');
	if (!gameMessageDiv) {
		gameMessageDiv = document.createElement('div');
		gameMessageDiv.id = 'game-message';
		gameMessageDiv.className = 'mt-4 text-center';
		document.getElementById('blackjack-container').appendChild(gameMessageDiv);
	}
	const updateMessage = (msg) => { gameMessageDiv.innerText = msg; };

	// Define suits and ranks for a standard deck
	const suits = ['C', 'D', 'H', 'S'];
	const ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

	// Create a new deck; card image filenames follow the pattern "rank-suit.png"
	function createDeck() {
		let deck = [];
		for (let suit of suits) {
			for (let rank of ranks) {
				let card = {
					rank: rank,
					suit: suit,
					value: getCardValue(rank),
					image: CARD_BASE_PATH + rank + '-' + suit + '.png'
				};
			deck.push(card);
			}
		}
		return deck;
	}

	// Get card value (face cards count as 10; Ace initially counts as 11)
	function getCardValue(rank) {
		if (rank === 'A') return 11;
		if (['K', 'Q', 'J'].includes(rank)) return 10;
		return parseInt(rank);
	}

	// Shuffle the deck using the Fisher-Yates algorithm
	function shuffle(deck) {
		for (let i = deck.length - 1; i > 0; i--) {
			const j = Math.floor(Math.random() * (i + 1));
			[deck[i], deck[j]] = [deck[j], deck[i]];
		}
	}

	// Compute the total value of a hand, adjusting for Aces if needed
	function computeHandValue(hand) {
		let value = 0;
		let aceCount = 0;
		hand.forEach(card => {
			value += card.value;
			if (card.rank === 'A') aceCount++;
		});
		// Adjust Aces from 11 to 1 if total is over 21
		while (value > 21 && aceCount > 0) {
			value -= 10;
			aceCount--;
		}
		return value;
	}

	// Create a card element with its image. If faceDown is true, use the card back image.
	function createCardElement(card, faceDown = false) {
		const cardDiv = document.createElement('div');
		cardDiv.classList.add('card');
		const imgUrl = faceDown ? CARD_PLACEHOLDER : card.image;
		cardDiv.style.backgroundImage = "url(" + imgUrl + ")";
		return cardDiv;
	  }	  

	// Render player and dealer hands. For the dealer, keep the second card face down if needed.
	function renderHands(revealDealer = false) {
		playerHandDiv.innerHTML = '';
		dealerHandDiv.innerHTML = '';

		playerHand.forEach(card => {
			playerHandDiv.appendChild(createCardElement(card));
		});

		dealerHand.forEach((card, index) => {
			// Show dealer's first card; second card is face down until revealDealer is true.
			let faceDown = (index === 1 && !revealDealer);
			dealerHandDiv.appendChild(createCardElement(card, faceDown));
		});
	}

	// Start a new game: reset deck and hands, shuffle, and deal initial cards.
	function startGame() {
		deck = createDeck();
		shuffle(deck);
		playerHand = [];
		dealerHand = [];
		gameOver = false;
		playerStands = false;
		updateMessage('');

		// Deal two cards each
		playerHand.push(deck.pop());
		dealerHand.push(deck.pop());
		playerHand.push(deck.pop());
		dealerHand.push(deck.pop());
		renderHands();

		// Check for immediate Blackjack
		if (computeHandValue(playerHand) === 21) {
			updateMessage("Blackjack! You win!");
			gameOver = true;
		}
	}

	// Player takes a hit: add a card and check for bust or 21.
	function playerHit() {
		if (gameOver || playerStands) return;
		playerHand.push(deck.pop());
		renderHands();
		let playerValue = computeHandValue(playerHand);
		if (playerValue > 21) {
			updateMessage("Bust! You lose.");
			gameOver = true;
		} else if (playerValue === 21) {
			updateMessage("You reached 21! Now stand.");
		}
	}

	// Player stands; dealer reveals card and hits until reaching 17 or more.
	function playerStand() {
		if (gameOver) return;
		playerStands = true;
		renderHands(true); // Reveal dealer's face-down card

		let dealerValue = computeHandValue(dealerHand);
		while (dealerValue < 17) {
			dealerHand.push(deck.pop());
			dealerValue = computeHandValue(dealerHand);
			renderHands(true);
		}

		// Determine the winner
		let playerValue = computeHandValue(playerHand);
		if (dealerValue > 21) {
			updateMessage("Dealer busts! You win.");
		} else if (dealerValue === playerValue) {
			updateMessage("Push. It's a tie.");
		} else if (dealerValue > playerValue) {
			updateMessage("Dealer wins.");
		} else {
			updateMessage("You win!");
		}
		gameOver = true;
	}

	// Attach event listeners to the buttons
	dealButton.addEventListener('click', startGame);
	hitButton.addEventListener('click', playerHit);
	standButton.addEventListener('click', playerStand);

	// Modal logic
	const modal = document.getElementById("rulesModal");
	const closeBtn = document.querySelector("#rulesModal .close");

	closeBtn.addEventListener("click", function() {
		modal.style.display = "none";
	});

	// Optionally, close modal when clicking outside the modal content
	window.addEventListener("click", function(event) {
		if (event.target === modal) {
		modal.style.display = "none";
		}
	});
});