
        const fileInput = document.getElementById('image');
        const uploadInput = document.querySelector('.upload-input');
        const preview = document.getElementById('preview');
        const previewText = document.getElementById('previewText');
        const resultModal = document.getElementById('resultModal');
        const resultText = document.getElementById('resultText');
        const modalContent = document.querySelector('.modal-content');

        function handleFile(file) {
            if (!file) {
                preview.hidden = true;
                previewText.textContent = 'No image selected yet.';
                return;
            }
            const reader = new FileReader();
            reader.onload = e => {
                preview.src = e.target.result;
                preview.hidden = false;
                previewText.textContent = 'Preview loaded. Press Analyze Face to predict.';
            };
            reader.readAsDataURL(file);
        }

        fileInput.addEventListener('change', event => {
            const file = event.target.files[0];
            handleFile(file);
        });

        ['dragenter', 'dragover'].forEach(eventName => {
            uploadInput.addEventListener(eventName, event => {
                event.preventDefault();
                event.stopPropagation();
                uploadInput.classList.add('dragover');
                previewText.textContent = 'Release to upload the image.';
            });
        });

        ['dragleave', 'dragend', 'drop'].forEach(eventName => {
            uploadInput.addEventListener(eventName, event => {
                event.preventDefault();
                event.stopPropagation();
                if (eventName === 'drop') {
                    const droppedFiles = event.dataTransfer?.files;
                    if (droppedFiles?.length) {
                        const file = droppedFiles[0];
                        fileInput.files = droppedFiles;
                        handleFile(file);
                    }
                }
                uploadInput.classList.remove('dragover');
            });
        });

        uploadInput.addEventListener('dragover', event => {
            event.dataTransfer.dropEffect = 'copy';
        });

        function showModal(message) {
            // prepare UI
            resultText.style.opacity = '0';
            const loader = document.getElementById('modalLoader');
            const bar = document.getElementById('progressBar');
            loader.style.display = 'flex';
            bar.style.width = '0%';
            resultModal.classList.add('show');
            modalContent.classList.remove('result-ready');

            // animate progress
            let progress = 0;
            const percentEl = document.getElementById('progressPercent');
            let cancelled = false;
            // wire cancel button
            const cancelBtn = document.getElementById('cancelBtn');
            if (cancelBtn) {
                cancelBtn.disabled = false;
                cancelBtn.onclick = () => {
                    cancelled = true;
                };
            }

            const interval = setInterval(() => {
                if (cancelled) {
                    clearInterval(interval);
                    loader.style.display = 'none';
                    percentEl.textContent = '0%';
                    resultText.textContent = 'Analysis cancelled.';
                    resultText.style.opacity = '1';
                    modalContent.classList.add('result-ready');
                    return;
                }
                const step = 6 + Math.round(Math.random() * 8);
                progress = Math.min(100, progress + step);
                bar.style.width = progress + '%';
                percentEl.textContent = progress + '%';
                if (progress >= 100) {
                    clearInterval(interval);
                    // hide loader and reveal result
                    loader.style.display = 'none';
                    percentEl.textContent = '100%';
                    resultText.textContent = message;
                    resultText.style.opacity = '1';
                    modalContent.classList.add('result-ready');
                }
            }, 120);
        }

        function closeModal() {
            resultModal.classList.remove('show');
            modalContent.classList.remove('result-ready');
        }

        document.addEventListener('keydown', event => {
            if (event.key === 'Escape') {
                closeModal();
            }
        });

        
    