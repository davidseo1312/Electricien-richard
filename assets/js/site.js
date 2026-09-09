/* Electricien Richard - JS minimal (menu + carte differee). Aucune dependance. */
(function () {
  "use strict";

  /* ---- Menu mobile ---- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", String(!open));
      toggle.setAttribute("aria-expanded", String(!open));
      document.body.style.overflow = !open ? "hidden" : "";
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A" && window.innerWidth < 1080) {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      }
    });
    window.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.getAttribute("data-open") === "true") {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
        toggle.focus();
      }
    });
  }

  /* ---- Carte Leaflet : chargee seulement a l'approche du viewport ---- */
  var mapEl = document.getElementById("map");
  if (!mapEl || !("IntersectionObserver" in window)) return;

  var loaded = false;
  function loadAsset(tag, attrs) {
    return new Promise(function (resolve, reject) {
      var el = document.createElement(tag);
      Object.keys(attrs).forEach(function (k) { el.setAttribute(k, attrs[k]); });
      el.onload = resolve;
      el.onerror = reject;
      document.head.appendChild(el);
    });
  }

  function initMap() {
    if (loaded) return;
    loaded = true;
    var points = [];
    try { points = JSON.parse(mapEl.getAttribute("data-points") || "[]"); } catch (e) { points = []; }

    var cssSrc = mapEl.getAttribute("data-css");
    var jsSrc = mapEl.getAttribute("data-js");

    loadAsset("link", { rel: "stylesheet", href: cssSrc })
      .then(function () {
        return loadAsset("script", { src: jsSrc });
      })
      .then(function () {
        var map = L.map(mapEl, {
          scrollWheelZoom: false,
          attributionControl: true
        }).setView([47.85, -2.4], 7);

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
          maxZoom: 18,
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        var bounds = [];
        points.forEach(function (p) {
          var isDept = p.type === "dept";
          var marker = L.circleMarker([p.lat, p.lon], {
            radius: isDept ? 11 : 7,
            color: "#111827",
            weight: 2,
            fillColor: isDept ? "#FACC15" : "#EAB308",
            fillOpacity: 0.9
          }).addTo(map);
          var html = '<strong>' + p.name + "</strong>";
          if (p.sub) html += "<br>" + p.sub;
          if (p.url) html += '<br><a href="' + p.url + '">Voir la page</a>';
          marker.bindPopup(html);
          bounds.push([p.lat, p.lon]);
        });
        if (bounds.length > 1) map.fitBounds(bounds, { padding: [36, 36] });
        else if (bounds.length === 1) map.setView(bounds[0], 10);

        mapEl.setAttribute("data-ready", "true");
      })
      .catch(function () {
        mapEl.innerHTML =
          '<p class="map-fallback">La carte interactive n\'a pas pu se charger. ' +
          'Les zones couvertes restent listees ci-dessous.</p>';
      });
  }

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { initMap(); io.disconnect(); }
      });
    },
    { rootMargin: "300px" }
  );
  io.observe(mapEl);
})();

/* ---- Formulaires : validation accessible + anti-spam ---------------------- */
(function () {
  "use strict";
  var forms = document.querySelectorAll("form.form");
  if (!forms.length) return;

  var MESSAGES = {
    valueMissing: "Ce champ est nécessaire pour traiter votre demande.",
    tooShort: "Merci de préciser un peu plus.",
    typeMismatch: "Le format saisi ne semble pas valide.",
    patternMismatch: "Merci de saisir un numéro de téléphone valide.",
    checkbox: "Merci d'accepter l'utilisation de vos informations."
  };

  function messageFor(field) {
    var v = field.validity;
    if (field.type === "checkbox") return MESSAGES.checkbox;
    if (v.valueMissing) return MESSAGES.valueMissing;
    if (v.tooShort) return MESSAGES.tooShort;
    if (v.typeMismatch) return MESSAGES.typeMismatch;
    if (v.patternMismatch) return MESSAGES.patternMismatch;
    return "Merci de vérifier ce champ.";
  }

  function errorSlot(field) {
    var holder = field.closest(".field") || field.closest(".consent") || field.parentNode;
    var slot = holder.querySelector(".error-msg");
    if (!slot) {
      slot = document.createElement("span");
      slot.className = "error-msg";
      slot.id = (field.id || "champ") + "-erreur";
      holder.appendChild(slot);
    }
    return slot;
  }

  function showError(field) {
    var slot = errorSlot(field);
    slot.textContent = messageFor(field);
    field.setAttribute("aria-invalid", "true");
    field.setAttribute("aria-describedby", slot.id);
  }

  function clearError(field) {
    var slot = errorSlot(field);
    slot.textContent = "";
    field.removeAttribute("aria-invalid");
    field.removeAttribute("aria-describedby");
  }

  Array.prototype.forEach.call(forms, function (form) {
    form.setAttribute("novalidate", "novalidate");
    var status = form.querySelector(".form-status");
    var fields = form.querySelectorAll("input:not([tabindex='-1']), select, textarea");

    Array.prototype.forEach.call(fields, function (field) {
      field.addEventListener("blur", function () {
        if (field.value || field.required) {
          field.checkValidity() ? clearError(field) : showError(field);
        }
      });
      field.addEventListener("input", function () {
        if (field.getAttribute("aria-invalid") && field.checkValidity()) clearError(field);
      });
    });

    form.addEventListener("submit", function (e) {
      /* Champ piège rempli = robot : on abandonne silencieusement. */
      var trap = form.querySelector('input[name="site_web"]');
      if (trap && trap.value) { e.preventDefault(); return; }

      var premier = null;
      Array.prototype.forEach.call(fields, function (field) {
        if (!field.checkValidity()) {
          showError(field);
          if (!premier) premier = field;
        } else {
          clearError(field);
        }
      });

      if (premier) {
        e.preventDefault();
        if (status) {
          status.hidden = false;
          status.setAttribute("data-state", "ko");
          status.textContent =
            "Votre demande n'a pas pu être envoyée : un champ reste à compléter.";
        }
        premier.focus();
        premier.scrollIntoView({ block: "center", behavior: "smooth" });
        return;
      }

      if (status) {
        status.hidden = false;
        status.setAttribute("data-state", "ok");
        status.textContent = form.getAttribute("action").indexOf("mailto:") === 0
          ? "Votre logiciel de messagerie va s'ouvrir avec votre demande pré-remplie. "
            + "Pour une urgence, appelez plutôt le 02 20 06 00 75."
          : "Merci, votre demande est envoyée. Vous serez recontacté au numéro indiqué.";
      }
    });
  });
})();
