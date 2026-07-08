# This environment cannot run AI image generation; mascot art is code-drawn

Checked 2026-06-12 in the Claude Code web container for this repo: no image-gen
MCP tools or API keys; huggingface.co and download.pytorch.org return 403 under
the network policy, so diffusion weights cannot be fetched (CPU 4 cores / 15 GB
RAM would otherwise suffice); github.com and raw.githubusercontent.com are
reachable (e.g. rembg's u2net.onnx is obtainable for background removal of
user-supplied art). Consequence: Gyeongtae mascot art ships as hand-authored SVG
(tools/assets/, comic + flat editions). Unlocks if true illustration is wanted:
allowlist huggingface.co in the environment's network policy, or have SETI
upload art made elsewhere and composite it into the header template.
