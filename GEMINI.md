# Hostile Secured Session (CTF Challenge)

## Project Overview

This directory contains the "Hostile Secured Session" CTF challenge. It is a Python-based project that utilizes gRPC for communication. The core logic and protobuf definitions are provided as compiled Python extensions (`.so` files), making this likely a reverse-engineering or network analysis challenge.

**Goal:** Analyze the code/client behavior and find the flag.
**Rules:** Never modify anything in `build_original` directory.

## Directory Structure

*   **`src/build1/`**: Contains the main Python client script.
    *   `test-client_v1.0.0.py`: The entry point script to run the client.
    *   `test-client.py.original`: Original version of the script that is prohibited of modify.
*   **Root Directory**: Contains the compiled extensions required by the client.
    *   `client.cpython-311-x86_64-linux-gnu.so`: Compiled client logic (likely containing `create_client_channel`, `PoskaShipStub`).
    *   `common.cpython-311-x86_64-linux-gnu.so`: Common utilities (likely containing `message_to_dict`).
    *   `poskaship_pb2...so`: Compiled Protobuf/gRPC definitions.
*   **`pyproject.toml`**: Project configuration using `setuptools` and `Cython`, seemingly set up to package the pre-compiled binaries.

## Usage

### Prerequisites

*   **Python 3.11**: The `.so` files are specifically compiled for CPython 3.11 on x86_64 Linux (`cpython-311-x86_64-linux-gnu`). Using a different Python version will likely result in import errors.

### Running the Client
Use the virtual environment in the directory `.p3-11`.
To use the virtual environment, we use:
```bash
source ./.p3-11/bin/activate
```


To run the client, use the provided script in `src/build1`.
```bash
python3.11 src/build1/test-client_v1.0.0.py
```

By default, it connects to `www.passetonhack.fr`. You can specify a different remote host:
    
```bash
python3.11 src/build1/test-client_v1.0.0.py <remote_host>
```

## Investigation Notes
*   **Logs:** You must log every discovery, failures, success into `search.md`. Log also all your thinking into `search.md`
*   **Reflexion**: Do not loop, or try indefinitely. Do not hallucinate. If stuck, or failing, stop and report. Process step by step.
*   **Black Box Analysis:** Since the core logic is in `.so` files, you cannot simply read the source code for `client` or `common`. You may need to use tools like `objdump`, `ghidra`, or dynamic analysis (running it and observing behavior/traffic) to understand how it works.
*   **gRPC:** The project uses gRPC. Understanding `poskaship.proto` (which can be inferred or reconstructed from the `pb2` module) will be helpful.
