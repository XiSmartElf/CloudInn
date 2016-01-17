
// Vars

var obj = {
	paused: true
}

var tlLandscape = new TimelineMax();
var tlPower = new TimelineMax(obj);
var tlReady = new TimelineMax(obj);
var tlButton = new TimelineMax(obj);
var tlSwitch = new TimelineMax(obj);

// Set

TweenMax.set('#camera--view', {
	transformOrigin: 'center bottom',
	scale: .65
})

TweenMax.set(['.sun', '#camera--circle'], {
	transformOrigin: 'center'
})

// Timelines

tlLandscape
	.to('.sun', 1.75, {
		scale: .5,
		repeat: -1,
		yoyo: true,
		ease: Sine.easeIn
	}, 'start')
	.staggerTo('.cloud', 4.5, {
		cycle: {
			// x: [-50, 50, -75, 50, -75]
			x: [-120, 80, -105, 80, -120]
		},
		repeat: -1,
		yoyo: true,
		ease: Power1.easeInOut
	}, 0, 'start');

tlButton
	.to('#power', .25, {
		fill: '#c50000'
	});

tlReady
	.to('#ready', .25, {
		fill: '#8dff8d'
	});

tlSwitch
	.to('#camera--switch', .25, {
		x: 15
	})
	.to('#light', .25, {
		fill: '#ffa002'
	}, 0);

tlPower
	.to('#power', .35, {
		y: 5
	})
	.to('#flash', .25, {
		attr: {
			r: 500
		},
		autoAlpha: 0
	}, '-=.2')
	.to('#power', .35, {
		y: 0
	})
	.to('#photo', .35, {
		autoAlpha: 0
	}, '-=.75')
	.to('#photo', .25, {
		autoAlpha: 1
	})

// Draggable

Draggable.create('#camera--view', {
	bounds: '#rect',
	dragResistance: -1.55,
	onDragStart: start,
	onDrag: rotate
})

function rotate() {
	TweenMax.to('#camera--circle', .65, {
		rotation: '+=25'
	})
}

function start() {
	tlButton.play();
	tlReady.reverse();
}

// 

document.getElementById('power').addEventListener('click', function() {
	if (tlButton.progress() > 0) {
		tlPower.restart();
		tlReady.play();	
		tlButton.reverse();	
	}
})

document.getElementById('camera--switch').addEventListener('click', function() {

	if (tlLandscape.isActive()) {
		tlLandscape.pause();
		tlSwitch.play();
	} else {
		tlLandscape.play();
		tlSwitch.reverse();
	}
});

// Helpers

function random() {
	return (Math.random() * 4 - 2) * 60;
}
