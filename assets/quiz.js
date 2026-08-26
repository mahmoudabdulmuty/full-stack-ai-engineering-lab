/* ai-python-tutor quiz engine
   Reusable interactive component for assessment pages.

   HTML contract:
   - MCQ card:  <div class="card mcq" data-qid="q1">
                  <div class="options"><button class="option" data-correct="true|false">…</button></div>
                  <div class="feedback"></div>
                  <div class="explanation">…</div>
                </div>
   - Typed card (open question): <div class="card typed" data-qid="q2" data-required='f"|.2f'>
                  <textarea class="answer-box" rows="3"></textarea>
                  <button class="check">I'm done — check</button>
                  <div class="feedback"></div>
                  <div class="explanation">… key points / hints …</div>
                </div>
     Optional data-required: pipe-separated markers. When present the answer is auto-validated;
     when absent the question is self-assessed against the key points in the explanation.
   - Reveal toggle: <button class="reveal" data-reveal="a1">…</button> paired with <div class="model-answer" id="a1">…</div>
   - Trap toggle:   <button class="reveal reveal-trap" data-reveal="t1">…</button> paired with <div class="trap" id="t1">…</div>
   - Score bar:     <div id="scorebar"><div class="bar"><i></i></div><span id="scoretext"></span></div>
*/

(function () {
  "use strict";

  var barFill = document.querySelector("#scorebar .bar i");
  var scoreText = document.querySelector("#scoretext");
  var total = document.querySelectorAll(".mcq, .typed").length;
  var answered = 0;
  var correct = 0;

  function updateScore() {
    var pct = total === 0 ? 0 : Math.round((answered / total) * 100);
    if (barFill) barFill.style.width = pct + "%";
    if (scoreText) {
      scoreText.textContent = answered + " / " + total + " attempted · " + correct + " auto-correct";
    }
  }

  function finish(card, ok, message) {
    card.dataset.answered = "1";
    answered++;
    var feedback = card.querySelector(".feedback");
    if (feedback) {
      feedback.textContent = message;
      feedback.className = ok ? "feedback ok" : "feedback no";
    }
    if (ok) correct++;
    updateScore();
  }

  // --- MCQ single-select ---
  document.querySelectorAll(".mcq").forEach(function (card) {
    var opts = card.querySelectorAll(".option");
    var feedback = card.querySelector(".feedback");
    var explanation = card.querySelector(".explanation");

    opts.forEach(function (opt) {
      opt.addEventListener("click", function () {
        if (card.dataset.answered) return;
        card.dataset.answered = "1";
        answered++;
        var isRight = opt.dataset.correct === "true";
        opts.forEach(function (o) { o.disabled = true; });

        if (isRight) {
          opt.classList.add("is-correct");
          correct++;
          if (feedback) {
            feedback.textContent = "Correct.";
            feedback.className = "feedback ok";
          }
        } else {
          opt.classList.add("is-wrong");
          opts.forEach(function (o) {
            if (o.dataset.correct === "true") o.classList.add("is-correct");
          });
          if (feedback) {
            feedback.textContent = "Not quite — check the explanation below.";
            feedback.className = "feedback no";
          }
        }
        if (explanation) explanation.classList.add("show");
        updateScore();
      });
    });
  });

  // --- Typed answers ---
  document.querySelectorAll(".typed").forEach(function (card) {
    var box = card.querySelector(".answer-box");
    var btn = card.querySelector(".check");
    var explanation = card.querySelector(".explanation");
    if (!box || !btn) return;

    btn.addEventListener("click", function () {
      if (card.dataset.answered) return;
      var raw = box.value.trim();
      if (raw.length === 0) {
        if (card.querySelector(".feedback")) {
          var fb = card.querySelector(".feedback");
          fb.textContent = "Empty answer — commit something first.";
          fb.className = "feedback no";
        }
        return;
      }

      var required = card.getAttribute("data-required");
      if (required) {
        var markers = required.split("|").map(function (m) { return m.trim(); });
        var missing = markers.filter(function (m) { return raw.indexOf(m) === -1; });
        if (missing.length === 0) {
          finish(card, true, "Looks right — the key markers are there.");
        } else if (missing.length < markers.length) {
          finish(card, false, "Almost. Missing marker: " + missing.join(", "));
        } else {
          finish(card, false, "Not there yet — check the explanation below.");
        }
      } else {
        finish(card, false, "Recorded. Now compare against the key points below — brutally honestly.");
      }
      if (explanation) explanation.classList.add("open");
      btn.disabled = true;
      box.readOnly = true;
    });
  });

  // --- reveal toggles (model answers + traps) ---
  document.querySelectorAll(".reveal").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var id = btn.dataset.reveal;
      var target = document.getElementById(id);
      if (!target) return;
      var open = target.classList.toggle("open");
      btn.textContent = open
        ? (btn.classList.contains("reveal-trap") ? "Hide the trap" : "Hide model answer")
        : (btn.classList.contains("reveal-trap") ? "Reveal the trap" : "Reveal model answer");
    });
  });

  // --- reset ---
  var resetBtn = document.getElementById("reset");
  if (resetBtn) {
    resetBtn.addEventListener("click", function () {
      document.querySelectorAll(".mcq").forEach(function (card) {
        delete card.dataset.answered;
        card.querySelectorAll(".option").forEach(function (o) {
          o.disabled = false;
          o.classList.remove("is-correct", "is-wrong");
        });
        var fb = card.querySelector(".feedback");
        if (fb) { fb.className = "feedback"; fb.textContent = ""; }
        var ex = card.querySelector(".explanation");
        if (ex) ex.classList.remove("show", "open");
      });
      document.querySelectorAll(".typed").forEach(function (card) {
        delete card.dataset.answered;
        var box = card.querySelector(".answer-box");
        var btn = card.querySelector(".check");
        if (box) { box.value = ""; box.readOnly = false; }
        if (btn) btn.disabled = false;
        var fb = card.querySelector(".feedback");
        if (fb) { fb.className = "feedback"; fb.textContent = ""; }
        var ex = card.querySelector(".explanation");
        if (ex) ex.classList.remove("show", "open");
      });
      answered = 0; correct = 0;
      updateScore();
    });
  }

  updateScore();
})();